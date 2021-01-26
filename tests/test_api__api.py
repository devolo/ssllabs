from unittest.mock import patch

import pytest

from ssllabs.api._api import _Api

try:
    from unittest.mock import AsyncMock
except ImportError:
    from asynctest import CoroutineMock as AsyncMock

from httpx import HTTPStatusError, Request, Response


class TestAPI:

    @pytest.mark.asyncio
    async def test_api(self):
        req = Request("GET", "")
        with patch("httpx._client.AsyncClient.get", new=AsyncMock(return_value=Response(401, request=req))):
            with pytest.raises(HTTPStatusError):
                await _Api()._call("")

    @pytest.mark.asyncio
    async def test_api_positive(self):
        req = Request("GET", "")
        with patch("httpx._client.AsyncClient.get", new=AsyncMock(return_value=Response(200, request=req))):
            r = await _Api()._call("")
            assert type(r) is Response
