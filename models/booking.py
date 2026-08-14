from dataclasses import asdict, dataclass
from typing import Any

@dataclass
class BookingDates:
    checkin: str
    checkout: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)

@dataclass
class Booking:
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
