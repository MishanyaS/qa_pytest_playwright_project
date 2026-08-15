from typing import Any

import httpx

from api.base_client import BaseClient
from models.booking import Booking


class BookingClient(BaseClient):
    def get_bookings(
        self,
        *,
        firstname: str | None = None,
        lastname: str | None = None,
        checkin: str | None = None,
        checkout: str | None = None,
    ) -> httpx.Response:
        params: dict[str, str] = {}

        if firstname is not None:
            params["firstname"] = firstname

        if lastname is not None:
            params["lastname"] = lastname

        if checkin is not None:
            params["checkin"] = checkin

        if checkout is not None:
            params["checkout"] = checkout

        return self.get("/booking", params=params or None)

    def get_booking(self, booking_id: int) -> httpx.Response:
        return self.get(f"/booking/{booking_id}")

    def create_booking(self, booking: Booking | dict[str, Any]) -> httpx.Response:
        payload = booking.to_dict() if isinstance(booking, Booking) else booking

        return self.post("/booking", json_data=payload)

    def update_booking(
        self, booking_id: int, booking: Booking | dict[str, Any], token: str
    ) -> httpx.Response:
        payload = booking.to_dict() if isinstance(booking, Booking) else booking

        return self.put(
            f"/booking/{booking_id}",
            headers={"Cookie": f"token={token}"},
            json_data=payload,
        )

    def partial_update_booking(
        self, booking_id: int, data: dict[str, Any], token: str
    ) -> httpx.Response:
        return self.patch(
            f"/booking/{booking_id}",
            headers={"Cookie": f"token={token}"},
            json_data=data,
        )

    def delete_booking(self, booking_id: int, token: str) -> httpx.Response:
        return self.delete(
            f"/booking/{booking_id}",
            headers={"Cookie": f"token={token}"},
        )
