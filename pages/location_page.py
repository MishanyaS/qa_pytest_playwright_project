from __future__ import annotations

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class LocationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.location_section: Locator = page.locator("#location")
        self.location_title: Locator = page.locator("#location h2")
        self.location_description: Locator = page.locator(
            "#location > .container > .text-center p"
        )

        self.map: Locator = page.locator("#location .pigeon-tiles-box")
        self.map_marker: Locator = page.locator("#location .pigeon-click-block")
        self.map_attribution: Locator = page.locator("#location .pigeon-attribution")

        self.contact_information: Locator = page.locator("#location .card-body").nth(1)
        self.contact_information_title: Locator = page.locator(
            "#location .card-body h3"
        )

        self.address_title: Locator = page.locator("#location .card-body h5").nth(0)
        self.address: Locator = page.locator("#location .card-body p").nth(0)

        self.phone_title: Locator = page.locator("#location .card-body h5").nth(1)
        self.phone: Locator = page.locator("#location .card-body p").nth(1)

        self.email_title: Locator = page.locator("#location .card-body h5").nth(2)
        self.email: Locator = page.locator("#location .card-body p").nth(2)

        self.getting_here_title: Locator = page.locator("#location .card-body h4")
        self.getting_here_description: Locator = page.locator(
            "#location .card-body h4 + p"
        )

    def open_location(self) -> None:
        self.location_section.wait_for(state="visible")

    def location_visible(self) -> bool:
        return self.is_visible(self.location_section)

    def location_title_visible(self) -> bool:
        return self.is_visible(self.location_title)

    def location_description_visible(self) -> bool:
        return self.is_visible(self.location_description)

    def map_visible(self) -> bool:
        return self.is_visible(self.map)

    def map_marker_visible(self) -> bool:
        return self.is_visible(self.map_marker)

    def contact_information_visible(self) -> bool:
        return self.is_visible(self.contact_information)

    def contact_information_title_visible(self) -> bool:
        return self.is_visible(self.contact_information_title)

    def getting_here_visible(self) -> bool:
        return self.is_visible(self.getting_here_title)

    def get_location_title(self) -> str:
        self.location_title.wait_for(state="visible")

        return self.get_text(self.location_title)

    def get_location_description(self) -> str:
        self.location_description.wait_for(state="visible")

        return self.get_text(self.location_description)

    def get_address(self) -> str:
        self.address.wait_for(state="visible")

        return self.get_text(self.address)

    def get_phone(self) -> str:
        self.phone.wait_for(state="visible")

        return self.get_text(self.phone)

    def get_email(self) -> str:
        self.email.wait_for(state="visible")

        return self.get_text(self.email)

    def get_getting_here_title(self) -> str:
        self.getting_here_title.wait_for(state="visible")

        return self.get_text(self.getting_here_title)

    def get_getting_here_description(self) -> str:
        self.getting_here_description.wait_for(state="visible")

        return self.get_text(self.getting_here_description)
