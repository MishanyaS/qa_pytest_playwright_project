from __future__ import annotations

import allure
import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage


@allure.epic("UI Tests")
@allure.feature("Home Page")
@pytest.mark.ui
@pytest.mark.regression
class TestHomePage:
    @allure.story("Home page navigation")
    @allure.title("Home page opens successfully")
    @allure.description(
        "Verifies that the Home page opens successfully and all main page sections are displayed."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_home_page_is_available(self, page: Page) -> None:
        home_page = HomePage(page)

        with allure.step("Open Home page"):
            home_page.open_home_page()

        with allure.step("Verify Home page URL"):
            assert home_page.get_url().startswith(home_page.URL)

        with allure.step("Verify navigation is visible"):
            assert home_page.navigation_visible()

        with allure.step("Verify Shady Meadows B&B brand is visible"):
            assert home_page.brand_visible()

        with allure.step("Verify Hero section is visible"):
            assert home_page.hero_visible()

        with allure.step("Verify Hero title"):
            assert home_page.hero_title_visible()
            assert home_page.get_hero_title() == "Welcome to Shady Meadows B&B"

        with allure.step("Verify Booking section is visible"):
            assert home_page.booking_visible()

        with allure.step("Verify Rooms section is visible"):
            assert home_page.rooms_visible()

        with allure.step("Verify Location section is visible"):
            assert home_page.location_visible()

        with allure.step("Verify Contact section is visible"):
            assert home_page.contact_visible()

        with allure.step("Verify Footer section is visible"):
            assert home_page.footer_visible()

    @allure.story("Booking navigation")
    @allure.title("Book Now button opens Booking section")
    @allure.description(
        "Verifies that clicking the Book Now button opens the Booking section."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_book_now_navigates_to_booking(self, page: Page) -> None:
        home_page = HomePage(page)

        with allure.step("Open Home page"):
            home_page.open_home_page()

        with allure.step("Open Book Now button"):
            home_page.open_booking()

        with allure.step("Verify Booking section is displayed"):
            assert home_page.booking_visible()

        with allure.step("Verify Booking section title"):
            assert (
                home_page.get_booking_title() == "Check Availability & Book Your Stay"
            )

        with allure.step("Verify Check Availability button is visible"):
            assert home_page.check_availability_visible()

        with allure.step("Verify Booking section URL anchor"):
            assert "#booking" in home_page.get_url()

    @allure.story("Rooms navigation")
    @allure.title("Rooms navigation opens Rooms section")
    @allure.description(
        "Verifies that the Rooms navigation link opens the Rooms section."
    )
    @pytest.mark.positive
    def test_rooms_navigation(self, page: Page) -> None:
        home_page = HomePage(page)

        with allure.step("Open Home page"):
            home_page.open_home_page()

        with allure.step("Click Rooms navigation link"):
            home_page.open_rooms()

        with allure.step("Verify Rooms section is displayed"):
            assert home_page.rooms_visible()

        with allure.step("Verify Rooms section title"):
            assert home_page.get_rooms_title() == "Our Rooms"

        with allure.step("Verify Rooms URL anchor"):
            assert "#rooms" in home_page.get_url()

    @allure.story("Rooms section")
    @allure.title("All rooms are displayed")
    @allure.description(
        "Verifies that all available rooms are displayed with names, images and booking links."
    )
    @pytest.mark.positive
    def test_rooms_are_displayed(self, page: Page) -> None:
        home_page = HomePage(page)

        with allure.step("Open Home page"):
            home_page.open_home_page()

        with allure.step("Verify Rooms section is displayed"):
            assert home_page.rooms_visible()

        with allure.step("Get room names"):
            room_names = home_page.get_room_names()

        with allure.step("Verify room count"):
            assert home_page.get_room_count() == 3

        with allure.step("Verify room names"):
            assert room_names == ["Single", "Double", "Suite"]

        with allure.step("Verify every room has an image"):
            assert home_page.get_room_image_count() == 3

        with allure.step("Verify every room has a booking link"):
            assert home_page.get_room_booking_link_count() == 3
