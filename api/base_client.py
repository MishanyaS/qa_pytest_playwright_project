import json
import logging
from typing import Any

import allure
import httpx

logger = logging.getLogger(__name__)


class BaseClient:
    def __init__(self, client: httpx.Client) -> None:
        self.client = client

    @staticmethod
    def _format_response_body(response: httpx.Response) -> str:
        try:
            return json.dumps(response.json(), indent=4, ensure_ascii=False)
        except (ValueError, json.JSONDecodeError):
            return response.text

    @staticmethod
    def _log_request(method: str, url: str, **kwargs: Any) -> None:
        logger.info("HTTP Request: %s %s", method.upper(), url)

        if kwargs.get("params"):
            logger.info("Query params: %s", kwargs["params"])

        if kwargs.get("json") is not None:
            logger.info("Request body: %s", kwargs["json"])

    @staticmethod
    def _log_response(response: httpx.Response) -> None:
        logger.info(
            "HTTP Response: %s %s", response.status_code, response.reason_phrase
        )

        logger.info("Response body: %s", BaseClient._format_response_body(response))

    @staticmethod
    def _attach_request_to_allure(method: str, url: str, **kwargs: Any) -> None:
        request_data = {
            "method": method.upper(),
            "url": url,
            "params": kwargs.get("params"),
            "headers": kwargs.get("headers"),
            "json": kwargs.get("json"),
        }

        allure.attach(
            json.dumps(
                request_data,
                indent=4,
                default=str,
                ensure_ascii=False,
            ),
            name="HTTP Request",
            attachment_type=allure.attachment_type.JSON,
        )

    @staticmethod
    def _attach_response_to_allure(response: httpx.Response) -> None:
        response_data = {
            "status_code": response.status_code,
            "reason": response.reason_phrase,
            "headers": dict(response.headers),
            "body": BaseClient._format_response_body(response),
        }

        allure.attach(
            json.dumps(
                response_data,
                indent=4,
                default=str,
                ensure_ascii=False,
            ),
            name="HTTP Response",
            attachment_type=allure.attachment_type.JSON,
        )

    def request(
        self,
        method: str,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        json_data: Any = None,
        timeout: float | None = None,
    ) -> httpx.Response:
        request_kwargs: dict[str, Any] = {
            "params": params,
            "headers": headers,
            "json": json_data,
        }

        if timeout is not None:
            request_kwargs["timeout"] = timeout

        self._log_request(method, url, **request_kwargs)

        response = self.client.request(method=method, url=url, **request_kwargs)

        self._log_response(response)

        self._attach_response_to_allure(response)

        return response

    def get(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        timeout: float | None = None,
    ) -> httpx.Response:
        return self.request(
            method="GET", url=url, params=params, headers=headers, timeout=timeout
        )

    def post(
        self,
        url: str,
        *,
        json_data: Any = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        timeout: float | None = None,
    ) -> httpx.Response:
        return self.request(
            method="POST",
            url=url,
            params=params,
            headers=headers,
            json_data=json_data,
            timeout=timeout,
        )

    def put(
        self,
        url: str,
        *,
        json_data: Any = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        timeout: float | None = None,
    ) -> httpx.Response:
        return self.request(
            method="PUT",
            url=url,
            params=params,
            headers=headers,
            json_data=json_data,
            timeout=timeout,
        )

    def patch(
        self,
        url: str,
        *,
        json_data: Any = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        timeout: float | None = None,
    ) -> httpx.Response:
        return self.request(
            method="PATCH",
            url=url,
            params=params,
            headers=headers,
            json_data=json_data,
            timeout=timeout,
        )

    def delete(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        timeout: float | None = None,
    ) -> httpx.Response:
        return self.request(
            method="DELETE", url=url, params=params, headers=headers, timeout=timeout
        )
