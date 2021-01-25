import json

import pytest

from ssllabs.api.status_codes import StatusCodes


class TestStatusCodes:

    @pytest.mark.asyncio
    async def test_status_codes(self, request, patch_httpx):
        patch_httpx.return_value._text = json.dumps(request.cls.status_details)
        s = StatusCodes()
        status_codes = await s.get()
        assert status_codes.statusDetails == request.cls.status_details["statusDetails"]
