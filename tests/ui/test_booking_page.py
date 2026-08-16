from __future__ import annotations

import allure
import pytest
from playwright.sync_api import Page

from pages.booking_page import BookingPage
from pages.home_page import HomePage


@allure.epic("UI Tests")
@allure.feature("Booking Page")
@pytest.mark.ui
@pytest.mark.regression
class TestBookingPage:
    @allure.story("Booking page")
    @allure.title("Booking form is displayed")
    @allure.description(
        "Verifies that the Booking section is displayed with the booking title, check-in and check-out fields and the Check Availability button."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_booking_form_is_displayed(self, page: Page) -> None:
        home_page = HomePage(page)
        booking_page = BookingPage(page)

        with allure.step("Open Home page"):
            home_page.open_home_page()

        with allure.step("Open Booking section"):
            home_page.open_booking()

        with allure.step("Verify Booking section is visible"):
            assert booking_page.booking_visible()

        with allure.step("Verify Booking title is visible"):
            assert booking_page.booking_title_visible()

        with allure.step("Verify Booking title"):
            assert (
                booking_page.get_booking_title()
                == "Check Availability & Book Your Stay"
            )

        with allure.step("Verify Check In field is visible"):
            assert booking_page.check_in_visible()

        with allure.step("Verify Check Out field is visible"):
            assert booking_page.check_in_visible()

        with allure.step("Verify Check Availability button is visible"):
            assert booking_page.check_availability_visible()

    @allure.story("Booking dates")
    @allure.title("Default booking dates are displayed")
    @allure.description(
        "Verifies that the Booking section contains populated Check In and Check Out date fields."
    )
    @pytest.mark.positive
    def test_default_booking_dates_are_displayed(self, page: Page) -> None:
        home_page = HomePage(page)
        booking_page = BookingPage(page)

        with allure.step("Open Home page"):
            home_page.open_home_page()

        with allure.step("Open Booking section"):
            home_page.open_booking()

        with allure.step("Get Check In date"):
            check_in = booking_page.get_check_in_value()

        with allure.step("Get Check Out date"):
            check_out = booking_page.get_check_out_value()

        with allure.step("Verify Check In date is populated"):
            assert check_in

        with allure.step("Verify Check Out date is populated"):
            assert check_out

        with allure.step("Verify Check In and Check Out dates are different"):
            assert check_in != check_out

    @allure.story("Room availability")
    @allure.title("Available rooms are displayed after checking availability")
    @allure.description(
        "Verifies that checking availability displays the available rooms with their booking options."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_available_rooms_are_displayed(self, page: Page) -> None:
        home_page = HomePage(page)
        booking_page = BookingPage(page)

        with allure.step("Open Home page"):
            home_page.open_home_page()

        with allure.step("Open Booking section"):
            home_page.open_booking()

        with allure.step("Check room availability"):
            booking_page.check_availability()

        with allure.step("Verify Rooms section is visible"):
            assert booking_page.rooms_section.is_visible()

        with allure.step("Get available room names"):
            room_names = booking_page.get_room_names()

        with allure.step("Verify vailable room count"):
            assert booking_page.get_room_count() == 3

        with allure.step("Verify room names"):
            assert room_names == ["Single", "Double", "Suite"]

        with allure.step("Verify every room has a booking link"):
            assert booking_page.get_room_booking_link_count() == 3

    @allure.story("Room booking")
    @allure.title("Single rooms booking opens successfully")
    @allure.description(
        "Verifies that the Single room booking link opens the corresponding room reservation page."
    )
    @pytest.mark.positive
    def test_single_room_booking(self, page: Page) -> None:
        home_page = HomePage(page)
        booking_page = BookingPage(page)

        with allure.step("Open Home page"):
            home_page.open_home_page()

        with allure.step("Open Booking section"):
            home_page.open_booking()

        with allure.step("Check room availability"):
            booking_page.check_availability()

        with allure.step("Open Single room booking"):
            booking_page.open_room_booking("Single")

        with allure.step("Verify reservation URL"):
            assert "/reservation/1" in booking_page.get_url()

        with allure.step("Verify check-in date is present in URL"):
            assert "checkin=" in booking_page.get_url()

        with allure.step("Verify check-out date is present in URL"):
            assert "checkout=" in booking_page.get_url()
