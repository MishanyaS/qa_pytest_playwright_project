from __future__ import annotations

import allure
import pytest
from playwright.sync_api import Page

from pages.contact_page import ContactPage
from pages.home_page import HomePage

@allure.epic("UI Tests")
@allure.feature("Contact Page")
@pytest.mark.ui
@pytest.mark.regression
class TestContactPage:
    @allure.story("Contact page")
    @allure.title("Contact form is displayed")
    @allure.description("Verifies that the Contact section is displayed with all required form fields and the Submit button.")
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_contact_form_is_displayed(self, page: Page) -> None:
        home_page = HomePage(page)
        contact_page = ContactPage(page)

        with allure.step("Open Home page"):
            home_page.open_home_page()

        with allure.step("Open Contact section"):
            home_page.open_contact()

        with allure.step("Verify Contact section is visible"):
            assert contact_page.contact_visible()

        with allure.step("Verify Contact title is visible"):
            assert contact_page.contact_title_visible()

        with allure.step("Verify Contact title"):
            assert contact_page.get_contact_title() == "Send Us a Message"

        with allure.step("Verify Name field is visible"):
            assert contact_page.name_input_visible()

        with allure.step("Verify Email field is visible"):
            assert contact_page.email_input_visible()

        with allure.step("Verify Phone field is visible"):
            assert contact_page.phone_input_visible()

        with allure.step("Verify Subject field is visible"):
            assert contact_page.subject_input_visible()

        with allure.step("Verify Message field is visible"):
            assert contact_page.message_input_visible()

        with allure.step("Verify Submit button is visible"):
            assert contact_page.submit_button_visible()

    @allure.story("Contact form")
    @allure.title("Contact form accepts valid data")
    @allure.description("Verifies that valid contact information can be entered into all Contact form fields.")
    @pytest.mark.positive
    def test_contact_form_accepts_valid_data(self, page: Page) -> None:
        home_page = HomePage(page)
        contact_page = ContactPage(page)

        name = "John Doe"
        email = "john.doe@example.com"
        phone = "01234567890"
        subject = "Booking question"
        message = "I would like to ask about room availability."

        with allure.step("Open Home page"):
            home_page.open_home_page()

        with allure.step("Open Contact section"):
            home_page.open_contact()

        with allure.step("Fill Contact form"):
            contact_page.fill_contact_form(name=name, email=email, phone=phone, subject=subject, message=message)

        with allure.step("Verify Name value"):
            assert contact_page.get_name_value() == name

        with allure.step("Verify Email value"):
            assert contact_page.get_email_value() == email

        with allure.step("Verify Phone value"):
            assert contact_page.get_phone_value() == phone

        with allure.step("Verify Subject value"):
            assert contact_page.get_subject_value() == subject

        with allure.step("Verify Message value"):
            assert contact_page.get_message_value() == message

    @allure.story("Contact form")
    @allure.title("Contact form can be submitted")
    @allure.description("Verifies that the Contact form can be submitted after entering valid contact information.")
    @pytest.mark.positive
    def test_contact_form_can_be_submitted(self, page: Page) -> None:
        home_page = HomePage(page)
        contact_page = ContactPage(page)

        with allure.step("Open Home page"):
            home_page.open_home_page()

        with allure.step("Open Contact section"):
            home_page.open_contact()

        with allure.step("Fill Contact form"):
            contact_page.fill_contact_form(
                name="John Doe",
                email="john.doe@example.com",
                phone="01234567890",
                subject="Booking question",
                message="I would like to ask about room availability."
            )

        with allure.step("Submit Contact form"):
            contact_page.submit_form()

        with allure.step("Verify Contact section remains available"):
            assert contact_page.contact_visible()
