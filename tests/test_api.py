import dataclasses
import json
import re
from logging import Logger
from unittest.mock import patch

import pytest
from httpx import AsyncClient, HTTPStatusError, Request, Response

from ssllabs.api._api import _Api
from ssllabs.api.analyze import Analyze
from ssllabs.api.endpoint import Endpoint
from ssllabs.api.info import Info
from ssllabs.api.root_certs_raw import RootCertsRaw
from ssllabs.api.status_codes import StatusCodes
from ssllabs.data.endpoint import EndpointData
from ssllabs.data.host import HostData
from ssllabs.data.info import InfoData
from ssllabs.data.status_codes import StatusCodesData

try:
    from unittest.mock import AsyncMock
except ImportError:
    from asynctest import CoroutineMock as AsyncMock


class TestApi:

    API_CALLS = [(Endpoint,
                  EndpointData,
                  {
                      "host": "devolo.de",
                      "s": "195.201.179.93"
                  }),
                 (StatusCodes,
                  StatusCodesData,
                  {}),
                 (Info,
                  InfoData,
                  {}),
                 (Analyze,
                  HostData,
                  {
                      "host": "devolo.de"
                  })]

    @pytest.mark.asyncio
    async def test_api(self, request):
        req = Request("GET", "")
        with patch("httpx._client.AsyncClient.get",
                   new=AsyncMock(return_value=Response(200,
                                                       request=req,
                                                       content=json.dumps(request.cls.info)))):
            r = await _Api()._call("")  # pylint: disable=protected-access
            assert r.json() == request.cls.info

    @pytest.mark.asyncio
    async def test_api_raise(self):
        req = Request("GET", "")
        with patch("httpx._client.AsyncClient.get", new=AsyncMock(return_value=Response(401, request=req))), \
             pytest.raises(HTTPStatusError):
            await _Api()._call("")  # pylint: disable=protected-access

    @pytest.mark.asyncio
    @pytest.mark.parametrize("result, data, parameters", API_CALLS)
    async def test_api_calls(self, request, patch_httpx, result, data, parameters):
        test_data = re.sub(r"(?<!^)(?=[A-Z])", "_", result.__name__).lower()
        patch_httpx.return_value._text = json.dumps(getattr(request.cls, test_data))  # pylint: disable=protected-access
        api = result()
        api_data = await api.get(**parameters)
        assert type(api_data) is data
        assert dataclasses.asdict(api_data) == getattr(request.cls, test_data)

    @pytest.mark.asyncio
    async def test_root_certs_raw(self, request, patch_httpx):
        patch_httpx.return_value._text = json.dumps(request.cls.root_certs)  # pylint: disable=protected-access
        r = RootCertsRaw()
        root_certs = await r.get()
        assert type(root_certs) is str

    @pytest.mark.asyncio
    async def test_not_closing_client(self, mocker):
        api = _Api()
        api._needs_closing = False  # pylint: disable=protected-access
        spy = mocker.spy(AsyncClient, "aclose")
        del api
        assert spy.call_count == 0

    def test_unknown_parameter(self, mocker):
        spy = mocker.spy(Logger, "warning")
        api = _Api()
        api._verify_kwargs(["given"], ["known"])  # pylint: disable=protected-access
        assert spy.call_count == 1
