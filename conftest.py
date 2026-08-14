import logging
from collections.abc import Generator
from typing import Any, cast

import allure
import httpx
import pytest
from _pytest.fixtures import FixtureRequest
from _pytest.python import Function
from _pytest.reports import TestReport
from _pytest.runner import CallInfo
from faker import Faker
from playwright.sync_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
    sync_playwright,
)
from pluggy import Result

from api.base_client import BaseClient
from config import (
    ALLURE_REPORT,
    ALLURE_RESULTS,
    BASE_API_URL,
    BASE_UI_URL,
    BROWSER,
    DOWNLOADS_DIR,
    FAKER_LOCALE,
    HEADLESS,
    LOGS_DIR,
    PLAYWRIGHT_TIMEOUT,
    REQUEST_TIMEOUT,
    SCREENSHOTS_DIR,
    VIEWPORT_HEIGHT,
    VIEWPORT_WIDTH,
)

DIRECTORIES = (SCREENSHOTS_DIR, LOGS_DIR, DOWNLOADS_DIR, ALLURE_RESULTS, ALLURE_REPORT)

for directory in DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)


@pytest.fixture(scope="session")
def faker() -> Faker:
    return Faker(FAKER_LOCALE)


@pytest.fixture(scope="session")
def api_session() -> Generator[httpx.Client, None, None]:
    session = httpx.Client(
        base_url=BASE_API_URL,
        timeout=REQUEST_TIMEOUT,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )

    yield session

    session.close()


@pytest.fixture(scope="session")
def api_client(api_session: httpx.Client) -> BaseClient:
    return BaseClient(api_session)


@pytest.fixture(scope="session")
def timeout() -> int:
    return REQUEST_TIMEOUT


@pytest.fixture(scope="session")
def playwright() -> Generator[Playwright, None, None]:
    with sync_playwright() as playwright_instance:
        yield playwright_instance


@pytest.fixture(scope="session")
def browser(playwright: Playwright) -> Generator[Browser, None, None]:
    browser_types = {
        "chromium": playwright.chromium,
        "firefox": playwright.firefox,
        "webkit": playwright.webkit,
    }

    browser_type = browser_types.get(BROWSER)

    if browser_type is None:
        raise ValueError("Unsupported browser. Use one of: chromium, firefox, webkit.")

    browser_instance = browser_type.launch(headless=HEADLESS)

    yield browser_instance

    browser_instance.close()


@pytest.fixture
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    browser_context = browser.new_context(
        viewport={
            "width": VIEWPORT_WIDTH,
            "height": VIEWPORT_HEIGHT,
        },
        accept_downloads=True,
    )

    browser_context.set_default_timeout(PLAYWRIGHT_TIMEOUT)

    browser_context.set_default_navigation_timeout(PLAYWRIGHT_TIMEOUT)

    yield browser_context

    browser_context.close()


@pytest.fixture
def page(context: BrowserContext) -> Generator[Page, None, None]:
    page_instance = context.new_page()

    page_instance.goto(BASE_UI_URL)

    yield page_instance

    page_instance.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item: Function, call: CallInfo[Any]
) -> Generator[None, None, None]:
    outcome = yield

    report = cast(Result[TestReport], outcome).get_result()

    if report.when != "call":
        return

    if not report.failed:
        return

    page_instance = cast(Page | None, item.funcargs.get("page"))

    if page_instance is None:
        return

    screenshot = page_instance.screenshot(full_page=True)

    allure.attach(
        screenshot,
        name="Failure Screenshot",
        attachment_type=allure.attachment_type.PNG,
    )


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%H:%M:%S",
)

logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def test_logger(request: FixtureRequest) -> Generator[None, None, None]:
    logger.info("=" * 80)
    logger.info("START TEST -> %s", request.node.name)

    yield

    logger.info("END TEST -> %s", request.node.name)
    logger.info("=" * 80)
