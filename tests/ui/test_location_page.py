from __future__ import annotations

import allure
import pytest
from playwright.sync_api import Page

from pages.location_page import LocationPage
from pages.home_page import HomePage

@allure.epic("UI Tests")
@allure.feature("Location Page")
@pytest.mark.ui
@pytest.mark.regression
class TestLocationPage:
    @allure.story("Location navigation")
    @allure.title("Location section opens successfully")
    @allure.description("Verifies that the Location section can be open from the Home page and contains the expected title and description.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_location_section_opens(self, page: Page) -> None:
        home_page = HomePage(page)
        location_page = LocationPage(page)

        with allure.step("Open Home page"):
            home_page.open_home_page()

        with allure.step("Open Location section"):
            home_page.open_location()

        with allure.step("Verify Location section is visible"):
            assert location_page.location_visible()

        with allure.step("Verify Location title is visible"):
            assert location_page.location_title_visible()

        with allure.step("Verify Location title"):
            assert location_page.get_location_title() == "Our Location"

        with allure.step("Verify Location description"):
            assert location_page.get_location_description() == "Find us in the beautiful Newingtonfordburyshire countryside"

        with allure.step("Verify Location URL anchor"):
            assert "#location" in location_page.get_url()

    @allure.story("Location map")
    @allure.title("Location map is displayed")
    @allure.description("Verifies that the Location section contains a visible map and location marker.")
    @pytest.mark.positive
    def test_location_map_is_displayed(self, page: Page) -> None:
        home_page = HomePage(page)
        location_page = LocationPage(page)

        with allure.step("Open Home page"):
            home_page.open_home_page()

        with allure.step("Open Location section"):
            home_page.open_location()

        with allure.step("Verify map is visible"):
            assert location_page.map_visible()

        with allure.step("Verify map marker is visible"):
            assert location_page.map_marker_visible()

    @allure.story("Contact information")
    @allure.title("Location contact information is displayed")
    @allure.description("Verifies that the Location section displays the expected address, phone number and email address.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_contact_information_is_displayed(self, page: Page) -> None:
        home_page = HomePage(page)
        location_page = LocationPage(page)

        with allure.step("Open Home page"):
            home_page.open_home_page()

        with allure.step("Open Location section"):
            home_page.open_location()

        with allure.step("Verify Contact Information title"):
            assert location_page.get_text(location_page.contact_information_title) == "Contact Information"

        with allure.step("Verify address"):
            assert location_page.get_address() == "Shady Meadows B&B, Shadows valley, Newingtonfordburyshire, Dilbery, N1 1AA"

        with allure.step("Verify phone number"):
            assert location_page.get_phone() == "012345678901"

        with allure.step("Verify email"):
            assert location_page.get_email() == "fake@fakeemail.com"

    @allure.story("Getting Here")
    @allure.title("Getting Here information is displayed")
    @allure.description("Verifies that the Getting Here section contains the expected title and description..")
    @pytest.mark.positive
    def test_getting_here_information_is_displayed(self, page: Page) -> None:
        home_page = HomePage(page)
        location_page = LocationPage(page)

        with allure.step("Open Home page"):
            home_page.open_home_page()

        with allure.step("Open Location section"):
            home_page.open_location()

        with allure.step("Verify Getting Here section is visible"):
            assert location_page.getting_here_visible()

        with allure.step("Verify Getting Here title"):
            assert location_page.get_getting_here_title() == "Getting Here"

        with allure.step("Verify Getting Here description"):
            assert location_page.get_getting_here_description() == "Welcome to Shady Meadows, a delightful Bed & Breakfast nestled in the hills on Newingtonfordburyshire. A place so beautiful you will never want to leave. All our rooms have comfortable beds and we provide breakfast from the locally sourced supermarket. It is a delightful place."
