from datetime import date, timedelta

from faker import Faker

from models.booking import Booking, BookingDates

class BookingDataGenerator:
    def __init__(self, faker: Faker) -> None:
        self.faker = faker

    def create_booking(self) -> Booking:
        checkin = date.today() + timedelta(days=self.faker.random_int(min=1, max=30))

        checkout = checkin + timedelta(days=self.faker.random_int(min=1, max=14))

        return Booking(
            firstname=self.faker.first_name(),
            lastname=self.faker.last_name(),
            totalprice=self.faker.random_int(min=50, max=1000),
            depositpaid=self.faker.boolean(),
            bookingdates=BookingDates(checkin=checkin.isoformat(), checkout=checkout.isoformat()),
            additionalneeds=self.faker.random_element(
                elements=["Breakfast", "Dinner", "Lunch", "Extra bed", "Airport transfer"]
            )
        )
