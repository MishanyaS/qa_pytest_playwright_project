import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent

load_dotenv(PROJECT_ROOT / ".env")

BASE_API_URL = os.getenv("API_URL", "https://restful-booker.herokuapp.com/")

BASE_UI_URL = os.getenv("BASE_URL", "https://automationintesting.online/")

API_USERNAME = os.getenv("API_USERNAME", "admin")

API_PASSWORD = os.getenv("API_PASSWORD", "password123")

REQUEST_TIMEOUT = 10

BROWSER = os.getenv("BROWSER", "chromium")

HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

PLAYWRIGHT_TIMEOUT = int(os.getenv("PLAYWRIGHT_TIMEOUT", "10000"))

VIEWPORT_WIDTH = int(os.getenv("VIEWPORT_WIDTH", "1440"))

VIEWPORT_HEIGHT = int(os.getenv("VIEWPORT_HEIGHT", "900"))

FAKER_LOCALE = os.getenv("FAKER_LOCALE", "en_US")

SCREENSHOTS_DIR = PROJECT_ROOT / "screenshots"

LOGS_DIR = PROJECT_ROOT / "logs"

DOWNLOADS_DIR = PROJECT_ROOT / "downloads"

ALLURE_RESULTS = PROJECT_ROOT / "allure-results"

ALLURE_REPORT = PROJECT_ROOT / "allure-report"
