from playwright.sync_api import Locator, Page

from config import BASE_UI_URL
from pages.base_page import BasePage


class HomePage(BasePage):
    URL = BASE_UI_URL

    def __init__(self, page: Page):
        super().__init__(page)

        self.brand: Locator = page.locator("a.navbar-brand")
        self.navigation: Locator = page.locator("nav.navbar")

        self.rooms_link: Locator = page.locator("a.nav-link[href='/#rooms']")
        self.booking_link: Locator = page.locator("a.nav-link[href='/#booking']")
        self.amenities_link: Locator = page.locator("a.nav-link[href='/#amenities']")
        self.location_link: Locator = page.locator("a.nav-link[href='/#location']")
        self.contact_link: Locator = page.locator("a.nav-link[href='/#contact']")
        self.admin_link: Locator = page.locator("a.nav-link[href='/#admin']")

        self.hero_section: Locator = page.locator("section.hero")
        self.hero_title: Locator = page.locator("section.hero h1")
        self.hero_description: Locator = page.locator("section.hero p")
        self.book_now_button: Locator = page.locator("section.hero a[href='#booking']")

        self.booking_section: Locator = page.locator("#booking")
        self.booking_title: Locator = page.locator("#booking h3")
        self.check_in_input: Locator = page.locator("#booking input")
        self.check_out_input: Locator = page.locator("#booking input")
        self.check_availability_button: Locator = page.locator("#booking button")

        self.rooms_section: Locator = page.locator("#rooms")
        self.rooms_title: Locator = page.locator("#rooms h2")
        self.room_cards: Locator = page.locator("#rooms .room-card")
        self.room_titles: Locator = page.locator("#rooms .room-card h5")
        self.room_images: Locator = page.locator("#rooms .room-card img")
        self.room_booking_links: Locator = page.locator("#rooms .room-card a.btn")

        self.location_section: Locator = page.locator("#location")
        self.location_title: Locator = page.locator("#location h2")

        self.contact_section: Locator = page.locator("#contact")
        self.contact_title: Locator = page.locator("#contact h3")

        self.footer: Locator = page.locator("footer")

    def open_home_page(self) -> None:
        self.goto(self.URL)
        self.hero_title.wait_for(state="visible")

    def open_booking(self) -> None:
        self.book_now_button.wait_for(state="visible")
        self.book_now_button.click()
        self.booking_section.wait_for(state="visible")

    def open_rooms(self) -> None:
        self.rooms_link.wait_for(state="visible")
        self.rooms_link.click()
        self.rooms_section.wait_for(state="visible")

    def open_location(self) -> None:
        self.location_link.wait_for(state="visible")
        self.location_link.click()
        self.location_section.wait_for(state="visible")

    def open_contact(self) -> None:
        self.contact_link.wait_for(state="visible")
        self.contact_link.click()
        self.contact_section.wait_for(state="visible")

    def brand_visible(self) -> bool:
        return self.is_visible(self.brand)

    def navigation_visible(self) -> bool:
        return self.is_visible(self.navigation)

    def hero_visible(self) -> bool:
        return self.is_visible(self.hero_section)

    def hero_title_visible(self) -> bool:
        return self.is_visible(self.hero_title)

    def booking_visible(self) -> bool:
        return self.is_visible(self.booking_section)

    def rooms_visible(self) -> bool:
        return self.is_visible(self.rooms_section)

    def location_visible(self) -> bool:
        return self.is_visible(self.location_section)

    def contact_visible(self) -> bool:
        return self.is_visible(self.contact_section)

    def footer_visible(self) -> bool:
        return self.is_visible(self.footer)

    def check_availability_visible(self) -> bool:
        return self.is_visible(self.check_availability_button)

    def get_hero_title(self) -> str:
        self.hero_title.wait_for(state="visible")

        return self.get_text(self.hero_title)

    def get_booking_title(self) -> str:
        self.booking_title.wait_for(state="visible")

        return self.get_text(self.booking_title)

    def get_rooms_title(self) -> str:
        self.rooms_title.wait_for(state="visible")

        return self.get_text(self.rooms_title)

    def get_room_count(self) -> int:
        self.room_cards.first.wait_for(state="visible")

        return self.room_cards.count()

    def get_room_names(self) -> list[str]:
        self.room_titles.first.wait_for(state="visible")

        return self.room_titles.all_inner_texts()

    def get_room_image_count(self) -> int:
        self.room_images.first.wait_for(state="visible")

        return self.room_images.count()

    def get_room_booking_link_count(self) -> int:
        self.room_booking_links.first.wait_for(state="visible")

        return self.room_booking_links.count()
