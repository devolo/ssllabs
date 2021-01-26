import dataclasses
import json

import pytest

from ssllabs.api.analyze import Analyze
from ssllabs.api.endpoint import Endpoint
from ssllabs.api.info import Info
from ssllabs.api.status_codes import StatusCodes
from ssllabs.data.endpoint import EndpointData
from ssllabs.data.host import HostData
from ssllabs.data.info import InfoData
from ssllabs.data.status_codes import StatusCodesData


class TestEndpoint:

    test_data = [("endpoint",
                  Endpoint,
                  EndpointData,
                  {
                      "host": "a",
                      "s": "b"
                  }),
                 ("status_details",
                  StatusCodes,
                  StatusCodesData,
                  {}),
                 ("api_info",
                  Info,
                  InfoData,
                  {}),
                 ("analyze",
                  Analyze,
                  HostData,
                  {
                      "host": "devolo.de"
                  })]

    @pytest.mark.asyncio
    @pytest.mark.parametrize("path, class_name, dataclass_name, function_parameter", test_data)
    async def test_endpoint(self, request, patch_httpx, path, class_name, dataclass_name, function_parameter):
        patch_httpx.return_value._text = json.dumps(getattr(request.cls, path))
        e = class_name()
        endpoint = await e.get(**function_parameter)
        assert type(endpoint) is dataclass_name
        for key, value in getattr(request.cls, path).items():
            if not dataclasses.is_dataclass(getattr(endpoint, key)):
                if not type(getattr(endpoint, key)) is list:
                    assert value == getattr(endpoint, key)
                else:
                    if not all([dataclasses.is_dataclass(e) for e in getattr(endpoint, key)]):
                        assert value == getattr(endpoint, key)
                    else:
                        # TODO:
                        """Handle this!"""
            else:
                assert dataclasses.is_dataclass(getattr(endpoint, key))