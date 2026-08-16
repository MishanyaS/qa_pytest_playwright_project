from __future__ import annotations

import allure
import pytest
from jsonschema import validate

from api.auth_client import AuthClient
from schemas.auth_schema import AUTH_SCHEMA


@allure.epic("Restful Booker API")
@allure.feature("Authentication")
@pytest.mark.api
@pytest.mark.regression
class TestAuthentication:
    @allure.story("Authentication")
    @allure.title("Authentication token is created successfully")
    @allure.description(
        "Verifies that a valid username and password return a successful authentication response containing a valid token."
    )
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_create_auth_token(self, auth_client: AuthClient) -> None:
        with allure.step("Create authentication token"):
            response = auth_client.create_token(
                username="admin", password="password123"
            )

        with allure.step("Verify response status code"):
            assert response.status_code == 200

        with allure.step("Valid authentication response schema"):
            validate(instance=response.json(), schema=AUTH_SCHEMA)

    @allure.story("Authentication")
    @allure.title("Authentication fails with invalid credentials")
    @allure.description(
        "Verifies that authentication with invalid credentials returns the expected Bad credentials response."
    )
    @pytest.mark.negative
    def test_create_auth_token_with_invalid_credentials(
        self, auth_client: AuthClient
    ) -> None:
        with allure.step("Create authentication token"):
            response = auth_client.create_token(
                username="invalid_user", password="invalid_password123"
            )

        with allure.step("Verify response status code"):
            assert response.status_code == 200

        with allure.step("Verify authentication error reason"):
            response_data = response.json()

            assert response_data["reason"] == "Bad credentials"
