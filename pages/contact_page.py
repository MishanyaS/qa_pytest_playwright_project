from __future__ import annotations

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class ContactPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.contact_section: Locator = page.locator("#contact")
        self.contact_title: Locator = page.locator("#contact h3")

        self.name_input = page.locator("#contact input[data-testid='ContactName']")
        self.email_input = page.locator("#contact input[data-testid='ContactEmail']")
        self.phone_input = page.locator("#contact input[data-testid='ContactPhone']")
        self.subject_input = page.locator(
            "#contact input[data-testid='ContactSubject']"
        )
        self.message_input = page.locator(
            "#contact textarea[data-testid='ContactDescription']"
        )

        self.submit_button = page.locator("#contact button[type='button']")

    def open_contact(self) -> None:
        self.contact_section.wait_for(state="visible")

    def contact_visible(self) -> bool:
        return self.is_visible(self.contact_section)

    def contact_title_visible(self) -> bool:
        return self.is_visible(self.contact_title)

    def name_input_visible(self) -> bool:
        return self.is_visible(self.name_input)

    def email_input_visible(self) -> bool:
        return self.is_visible(self.email_input)

    def phone_input_visible(self) -> bool:
        return self.is_visible(self.phone_input)

    def subject_input_visible(self) -> bool:
        return self.is_visible(self.subject_input)

    def message_input_visible(self) -> bool:
        return self.is_visible(self.message_input)

    def submit_button_visible(self) -> bool:
        return self.is_visible(self.submit_button)

    def get_contact_title(self) -> str:
        self.contact_title.wait_for(state="visible")

        return self.get_text(self.contact_title)

    def fill_name(self, name: str) -> None:
        self.name_input.wait_for(state="visible")
        self.fill(self.name_input, name)

    def fill_email(self, email: str) -> None:
        self.email_input.wait_for(state="visible")
        self.fill(self.email_input, email)

    def fill_phone(self, phone: str) -> None:
        self.phone_input.wait_for(state="visible")
        self.fill(self.phone_input, phone)

    def fill_subject(self, subject: str) -> None:
        self.subject_input.wait_for(state="visible")
        self.fill(self.subject_input, subject)

    def fill_message(self, message: str) -> None:
        self.message_input.wait_for(state="visible")
        self.fill(self.message_input, message)

    def fill_contact_form(
        self, name: str, email: str, phone: str, subject: str, message: str
    ) -> None:
        self.fill_name(name)
        self.fill_email(email)
        self.fill_phone(phone)
        self.fill_subject(subject)
        self.fill_message(message)

    def get_name_value(self) -> str:
        self.name_input.wait_for(state="visible")

        return self.name_input.input_value()

    def get_email_value(self) -> str:
        self.email_input.wait_for(state="visible")

        return self.email_input.input_value()

    def get_phone_value(self) -> str:
        self.phone_input.wait_for(state="visible")

        return self.phone_input.input_value()

    def get_subject_value(self) -> str:
        self.subject_input.wait_for(state="visible")

        return self.subject_input.input_value()

    def get_message_value(self) -> str:
        self.message_input.wait_for(state="visible")

        return self.message_input.input_value()

    def submit_form(self) -> None:
        self.submit_button.wait_for(state="visible")
        self.submit_button.click()
