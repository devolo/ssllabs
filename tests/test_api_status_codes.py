from unittest.mock import patch

import pytest

from ssllabs.api.status_codes import StatusCodes

try:
    from unittest.mock import AsyncMock
except ImportError:
    from asynctest import CoroutineMock as AsyncMock


class TestStatusCodes:

    @pytest.mark.asyncio
    @pytest.mark.usefixtures("patch_httpx")
    async def test_status_codes(self, request):
        with patch("httpx._models.Response.json", return_value=request.cls.status_details):
            s = StatusCodes()
            status_codes = await s.get()
            assert status_codes.statusDetails == request.cls.status_details["statusDetails"]
