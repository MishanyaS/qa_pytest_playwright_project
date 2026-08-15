BOOKING_ID_LIST_SCHEMA: dict = {
    "type": "array",
    "items": {
        "type": "object",
        "required": [
            "bookingid",
        ],
        "properties": {
            "bookingid": {
                "type": "integer",
                "minimum": 1,
            },
        },
        "additionalProperties": True,
    },
}

BOOKING_SCHEMA: dict = {
    "type": "object",
    "required": [
        "firstname",
        "lastname",
        "totalprice",
        "depositpaid",
        "bookingdates",
        "additionalneeds",
    ],
    "properties": {
        "firstname": {
            "type": "string",
            "minLength": 1,
        },
        "lastname": {
            "type": "string",
            "minLength": 1,
        },
        "totalprice": {
            "type": "integer",
            "minimum": 0,
        },
        "depositpaid": {
            "type": "boolean",
        },
        "bookingdates": {
            "type": "object",
            "required": [
                "checkin",
                "checkout",
            ],
            "properties": {
                "checkin": {
                    "type": "string",
                    "format": "date",
                },
                "checkout": {
                    "type": "string",
                    "format": "date",
                },
            },
            "additionalProperties": True,
        },
        "additionalneeds": {
            "type": "string",
        },
    },
    "additionalProperties": True,
}

BOOKING_RESPONSE_SCHEMA: dict = {
    "type": "object",
    "required": [
        "firstname",
        "lastname",
        "totalprice",
        "depositpaid",
        "bookingdates",
    ],
    "properties": {
        "firstname": {
            "type": "string",
            "minLength": 1,
        },
        "lastname": {
            "type": "string",
            "minLength": 1,
        },
        "totalprice": {
            "type": "integer",
            "minimum": 0,
        },
        "depositpaid": {
            "type": "boolean",
        },
        "bookingdates": {
            "type": "object",
            "required": [
                "checkin",
                "checkout",
            ],
            "properties": {
                "checkin": {
                    "type": "string",
                    "format": "date",
                },
                "checkout": {
                    "type": "string",
                    "format": "date",
                },
            },
            "additionalProperties": True,
        },
        "additionalneeds": {
            "type": "string",
        },
    },
    "additionalProperties": True,
}

CREATE_BOOKING_SCHEMA: dict = {
    "type": "object",
    "required": [
        "bookingid",
        "booking",
    ],
    "properties": {
        "bookingid": {
            "type": "integer",
            "minimum": 1,
        },
        "booking": BOOKING_SCHEMA,
    },
    "additionalProperties": True,
}