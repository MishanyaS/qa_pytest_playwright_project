from typing import Any
import httpx

from api.base_client import BaseClient

class AuthClient(BaseClient):
    def create_token(self, username: str, password: str) -> httpx.Response:
        payload: dict[str, str] = {
            "username": username,
            "password": password,
        }

        return self.post("/auth", json_data=payload)

    def get_token(self, username: str, password: str) -> str:
        response = self.create_token(username=username, password=password)

        response.raise_for_status()

        data: dict[str, Any] = response.json()

        return str[data["token"]]
    