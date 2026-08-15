AUTH_SCHEMA: dict = {
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