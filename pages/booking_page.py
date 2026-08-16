from __future__ import annotations

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class BookingPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.booking_section: Locator = page.locator("#booking")
        self.booking_title: Locator = page.locator("#booking h3")

        self.check_in_input: Locator = page.locator(
            "#booking .react-datepicker-wrapper input"
        ).nth(0)
        self.check_out_input: Locator = page.locator(
            "#booking .react-datepicker-wrapper input"
        ).nth(1)
        self.check_in_label: Locator = page.locator("#booking label[for='checkin']")
        self.check_out_label: Locator = page.locator("#booking label[for='checkout']")
        self.check_availability_button: Locator = page.locator(
            "#booking button[type='button']"
        )

        self.rooms_section: Locator = page.locator("#rooms")
        self.room_cards: Locator = page.locator("#rooms .room-card")
        self.room_titles: Locator = page.locator("#rooms .room-card h5")
        self.room_booking_links: Locator = page.locator("#rooms .room-card a.btn")

    def open_booking(self) -> None:
        self.booking_section.wait_for(state="visible")

    def booking_visible(self) -> bool:
        return self.is_visible(self.booking_section)

    def booking_title_visible(self) -> bool:
        return self.is_visible(self.booking_title)

    def check_in_visible(self) -> bool:
        return self.is_visible(self.check_in_input)

    def check_out_visible(self) -> bool:
        return self.is_visible(self.check_out_input)

    def check_availability_visible(self) -> bool:
        return self.is_visible(self.check_availability_button)

    def get_booking_title(self) -> str:
        self.booking_title.wait_for(state="visible")

        return self.get_text(self.booking_title)

    def get_check_in_value(self) -> str:
        self.check_in_input.wait_for(state="visible")

        return self.check_in_input.input_value()

    def get_check_out_value(self) -> str:
        self.check_out_input.wait_for(state="visible")

        return self.check_out_input.input_value()

    def get_room_count(self) -> int:
        self.room_cards.first.wait_for(state="visible")

        return self.room_cards.count()

    def get_room_names(self) -> list[str]:
        self.room_titles.first.wait_for(state="visible")

        return self.room_titles.all_inner_texts()

    def get_room_booking_link_count(self) -> int:
        self.room_booking_links.first.wait_for(state="visible")

        return self.room_booking_links.count()

    def check_availability(self) -> None:
        self.check_availability_button.wait_for(state="visible")
        self.check_availability_button.click()

        self.rooms_section.wait_for(state="visible")

    def open_room_booking(self, room_name: str) -> None:
        room_card = self.room_cards.filter(
            has=self.page.locator("h5", has_text=room_name)
        )

        room_card.wait_for(state="visible")

        room_booking_link = room_card.locator("a.btn")
        room_booking_link.wait_for(state="visible")

        room_booking_link.click(trial=True)

        room_card = self.room_cards.filter(
            has=self.page.locator("h5", has_text=room_name)
        )
        room_booking_link = room_card.locator("a.btn")

        room_booking_link.click()
