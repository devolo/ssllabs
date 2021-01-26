import json

import pytest

from ssllabs.api.endpoint import Endpoint
from ssllabs.data.endpoint import EndpointData


class TestEndpoint:

    @pytest.mark.asyncio
    async def test_endpoint(self, request, patch_httpx):
        patch_httpx.return_value._text = json.dumps(request.cls.endpoint)
        e = Endpoint()
        endpoint = await e.get("a", "b")
        assert type(endpoint) is EndpointData
