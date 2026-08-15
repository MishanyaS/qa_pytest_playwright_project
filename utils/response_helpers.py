from typing import Any

import httpx
from jsonschema import FormatChecker, ValidationError, validate

from schemas.booking_schema import CREATE_BOOKING_SCHEMA

def get_booking_id_from_create_response(response: httpx.Response) -> int:
    response_data: Any = response.json()

    try:
        validate(instance=response_data, schema=CREATE_BOOKING_SCHEMA, format_checker=FormatChecker())
    except ValidationError as error:
        raise AssertionError(f"Invalid create booking response. Actual response: {response_data!r}") from error

    if not isinstance(response_data, dict):
        raise AssertionError(f"Create booking response must be a JSON object. Actual response: {response_data}")

    booking_id = response_data.get("bookingid")

    if not isinstance(booking_id, int):
        raise AssertionError(f"Create booking response contain integer. Actual response: {response_data!r}")

    return booking_id
