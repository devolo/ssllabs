import dataclasses
import re
from logging import Logger

import pytest
from httpx import AsyncClient, HTTPStatusError

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
    async def test_api(self, request, httpx_mock):
        httpx_mock.add_response(json=request.cls.info)
        r = await _Api()._call("")  # pylint: disable=protected-access
        assert r.json() == request.cls.info
        client = AsyncClient()
        r = await _Api(client)._call("")  # pylint: disable=protected-access
        await client.aclose()
        assert r.json() == request.cls.info

    @pytest.mark.asyncio
    async def test_api_raise(self, httpx_mock):
        httpx_mock.add_response(status_code=401)
        with pytest.raises(HTTPStatusError):
            await _Api()._call("")  # pylint: disable=protected-access

    @pytest.mark.asyncio
    @pytest.mark.parametrize("result, data, parameters", API_CALLS)
    async def test_api_calls(self, request, httpx_mock, result, data, parameters):
        test_data = re.sub(r"(?<!^)(?=[A-Z])", "_", result.__name__).lower()
        httpx_mock.add_response(json=getattr(request.cls, test_data))
        api = result()
        api_data = await api.get(**parameters)
        assert type(api_data) is data
        assert dataclasses.asdict(api_data) == getattr(request.cls, test_data)

    @pytest.mark.asyncio
    async def test_root_certs_raw(self, request, httpx_mock):
        httpx_mock.add_response(json=request.cls.root_certs)
        r = RootCertsRaw()
        root_certs = await r.get()
        assert type(root_certs) is str

    def test_unknown_parameter(self, mocker):
        spy = mocker.spy(Logger, "warning")
        api = _Api()
        api._verify_kwargs(["given"], ["known"])  # pylint: disable=protected-access
        assert spy.call_count == 1
