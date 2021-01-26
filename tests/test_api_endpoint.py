import dataclasses
import json

import pytest

from ssllabs.api.endpoint import Endpoint
from ssllabs.api.status_codes import StatusCodes
from ssllabs.data.endpoint import EndpointData
from ssllabs.data.status_codes import StatusCodesData


class TestEndpoint:

    test_data = [("endpoint",
                  Endpoint,
                  EndpointData,
                  {
                      "host": "a",
                      "endpoint_ip": "b"
                  }),
                 ("status_details",
                  StatusCodes,
                  StatusCodesData,
                  {})]

    @pytest.mark.asyncio
    @pytest.mark.parametrize("path, class_name, dataclass_name, function_parameter", test_data)
    async def test_endpoint(self, request, patch_httpx, path, class_name, dataclass_name, function_parameter):
        patch_httpx.return_value._text = json.dumps(getattr(request.cls, path))
        e = class_name()
        endpoint = await e.get(**function_parameter)
        assert type(endpoint) is dataclass_name
        for key, value in getattr(request.cls, path).items():
            if not dataclasses.is_dataclass(getattr(endpoint, key)):
                assert value == getattr(endpoint, key)
            else:
                assert dataclasses.is_dataclass(getattr(endpoint, key))
