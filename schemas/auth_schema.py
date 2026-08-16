from typing import Any

AUTH_SCHEMA: dict[str, Any] = {
    "type": "object",
    "required": [
        "token",
    ],
    "properties": {
        "token": {
            "type": "string",
            "minLength": 1,
        },
    },
    "additionalProperties": True,
}
