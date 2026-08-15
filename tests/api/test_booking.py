from typing import Any

import allure
import pytest
from jsonschema import FormatChecker, validate

from api.auth_client import AuthClient
from api.booking_client import BookingClient
from models.booking import Booking
from schemas.auth_schema import AUTH_SCHEMA
from schemas.booking_schema import BOOKING_ID_LIST_SCHEMA, BOOKING_SCHEMA, BOOKING_RESPONSE_SCHEMA, CREATE_BOOKING_SCHEMA
from utils.response_helpers import get_booking_id_from_create_response


@allure.epic("Restful Booker API")
@allure.feature("Authentication")
@pytest.mark.api
@pytest.mark.smoke
def test_create_auth_token(auth_client: AuthClient) -> None:
    with allure.step("Create authentication token"):
        response = auth_client.create_token(username="admin", password="password123")

    with allure.step("Verify response status code"):
        assert response.status_code == 200

    with allure.step("Valid authentication response schema"):
        validate(instance=response.json(), schema=AUTH_SCHEMA)

@allure.epic("Restful Booker API")
@allure.feature("Authentication")
@pytest.mark.api
@pytest.mark.regression
def test_create_auth_token_with_invalid_credentials(auth_client: AuthClient) -> None:
    with allure.step("Create authentication token"):
        response = auth_client.create_token(username="invalid_user", password="invalid_password123")

    with allure.step("Verify response status code"):
        assert response.status_code == 200

    with allure.step("Verify authentication error reason"):
        response_data = response.json()

        assert response_data["reason"] == "Bad credentials"

@allure.epic("Restful Booker API")
@allure.feature("Bookings")
@pytest.mark.api
@pytest.mark.smoke
def test_get_booking_ids(booking_client: BookingClient) -> None:
    with allure.step("Get booking IDs"):
        response = booking_client.get_bookings()

    with allure.step("Verify response status code"):
        assert response.status_code == 200

    with allure.step("Validate booking IDs schema"):
        validate(instance=response.json(), schema=BOOKING_ID_LIST_SCHEMA)

@allure.epic("Restful Booker API")
@allure.feature("Bookings")
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.parametrize(
    "firstname",
    [
        "John",
        "Mary",
        "Jim",
    ],
)
def test_get_bookings_by_firstname(booking_client: BookingClient, firstname: str) -> None:
    with allure.step(f"Get bookings filtered by firstname: {firstname}"):
        response = booking_client.get_bookings(firstname=firstname)

    with allure.step("Verify response status code"):
        assert response.status_code == 200

    with allure.step("Validate booking IDs schema"):
        validate(instance=response.json(), schema=BOOKING_ID_LIST_SCHEMA)

@allure.epic("Restful Booker API")
@allure.feature("Bookings")
@pytest.mark.api
@pytest.mark.smoke
def test_create_booking(booking_client: BookingClient, booking_data: Booking) -> None:
    with allure.step("Create booking"):
        response = booking_client.create_booking(booking_data)

    with allure.step("Verify response status code"):
        assert response.status_code == 200

    with allure.step("Validate create booking response schema"):
        validate(instance=response.json(), schema=CREATE_BOOKING_SCHEMA, format_checker=FormatChecker())

    with allure.step("Verify created booking data"):
        response_data = response.json()

        assert response_data["booking"]["firstname"] == booking_data.firstname
        assert response_data["booking"]["lastname"] == booking_data.lastname
        assert response_data["booking"]["totalprice"] == booking_data.totalprice
        assert response_data["booking"]["depositpaid"] == booking_data.depositpaid

@allure.epic("Restful Booker API")
@allure.feature("Bookings")
@pytest.mark.api
@pytest.mark.regression
def test_get_booking(booking_client: BookingClient) -> None:
    with allure.step("Get existing booking IDs"):
        booking_ids_response = booking_client.get_bookings()

    with allure.step("Verify booking IDs response"):
        assert booking_ids_response.status_code == 200

    booking_ids = booking_ids_response.json()

    with allure.step("Verify booking IDs list is not empty"):
        assert isinstance(booking_ids, list)
        assert booking_ids

    booking_id_data = booking_ids[0]

    with allure.step("Verify booking ID structure"):
        assert isinstance(booking_id_data, dict)
        assert "bookingid" in booking_id_data

    booking_id = booking_id_data["bookingid"]

    with allure.step(f"Get booking by ID: {booking_id}"):
        response = booking_client.get_booking(booking_id)

    with allure.step("Verify response status code"):
        assert response.status_code == 200

    with allure.step("Validate booking response schema"):
        validate(instance=response.json(), schema=BOOKING_RESPONSE_SCHEMA, format_checker=FormatChecker())

@allure.epic("Restful Booker API")
@allure.feature("Bookings")
@pytest.mark.api
@pytest.mark.regression
def test_get_booking_with_invalid_id(booking_client: BookingClient) -> None:
    invalid_booking_id = 999999999

    with allure.step(f"Get booking with invalid ID: {invalid_booking_id}"):
        response = booking_client.get_booking(invalid_booking_id)

    with allure.step("Verify response status code"):
        assert response.status_code == 404

@allure.epic("Restful Booker API")
@allure.feature("Bookings")
@pytest.mark.api
@pytest.mark.regression
def test_update_booking(
    booking_client: BookingClient,
    booking_data: Booking,
    auth_token: str,
) -> None:
    with allure.step("Create booking for update test"):
        create_response = booking_client.create_booking(
            booking_data,
        )

    with allure.step("Verify booking creation"):
        assert create_response.status_code == 200

    booking_id = get_booking_id_from_create_response(
        create_response,
    )

    updated_booking = Booking(
        firstname=booking_data.firstname,
        lastname=booking_data.lastname,
        totalprice=booking_data.totalprice + 100,
        depositpaid=not booking_data.depositpaid,
        bookingdates=booking_data.bookingdates,
        additionalneeds="Airport transfer",
    )

    with allure.step(
        f"Update booking with ID: {booking_id}",
    ):
        response = booking_client.update_booking(
            booking_id=booking_id,
            booking=updated_booking,
            token=auth_token,
        )

    with allure.step("Verify response status code"):
        assert response.status_code == 200

    with allure.step("Validate updated booking schema"):
        validate(
            instance=response.json(),
            schema=BOOKING_RESPONSE_SCHEMA,
            format_checker=FormatChecker(),
        )

    with allure.step("Verify updated booking data"):
        response_data = response.json()

        assert isinstance(response_data, dict)

        assert response_data["firstname"] == (
            updated_booking.firstname
        )

        assert response_data["totalprice"] == (
            updated_booking.totalprice
        )

        assert response_data["depositpaid"] == (
            updated_booking.depositpaid
        )

        assert response_data.get("additionalneeds") == (
            updated_booking.additionalneeds
        )


@allure.epic("Restful Booker API")
@allure.feature("Bookings")
@pytest.mark.api
@pytest.mark.regression
def test_partial_update_booking(
    booking_client: BookingClient,
    booking_data: Booking,
    auth_token: str,
) -> None:
    with allure.step("Create booking for partial update test"):
        create_response = booking_client.create_booking(
            booking_data,
        )

    with allure.step("Verify booking creation"):
        assert create_response.status_code == 200

    booking_id = get_booking_id_from_create_response(
        create_response,
    )

    partial_data: dict[str, Any] = {
        "firstname": "UpdatedName",
        "additionalneeds": "Extra bed",
    }

    with allure.step(
        f"Partially update booking with ID: {booking_id}",
    ):
        response = booking_client.partial_update_booking(
            booking_id=booking_id,
            data=partial_data,
            token=auth_token,
        )

    with allure.step("Verify response status code"):
        assert response.status_code == 200

    with allure.step("Validate booking schema"):
        validate(
            instance=response.json(),
            schema=BOOKING_RESPONSE_SCHEMA,
            format_checker=FormatChecker(),
        )

    with allure.step("Verify partial update"):
        response_data = response.json()

        assert isinstance(response_data, dict)
        assert response_data["firstname"] == "UpdatedName"
        assert response_data["additionalneeds"] == "Extra bed"


@allure.epic("Restful Booker API")
@allure.feature("Bookings")
@pytest.mark.api
@pytest.mark.regression
def test_delete_booking(
    booking_client: BookingClient,
    booking_data: Booking,
    auth_token: str,
) -> None:
    with allure.step("Create booking for delete test"):
        create_response = booking_client.create_booking(
            booking_data,
        )

    with allure.step("Verify booking creation"):
        assert create_response.status_code == 200

    booking_id = get_booking_id_from_create_response(
        create_response,
    )

    with allure.step(
        f"Delete booking with ID: {booking_id}",
    ):
        response = booking_client.delete_booking(
            booking_id=booking_id,
            token=auth_token,
        )

    with allure.step("Verify response status code"):
        assert response.status_code == 201

    with allure.step("Verify booking was deleted"):
        get_response = booking_client.get_booking(
            booking_id,
        )

        assert get_response.status_code == 404
