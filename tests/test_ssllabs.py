import dataclasses
from unittest.mock import patch

import pytest
from dacite import from_dict

from ssllabs import Ssllabs
from ssllabs.api.analyze import Analyze
from ssllabs.data.host import HostData
from ssllabs.data.info import InfoData
from ssllabs.data.status_codes import StatusCodesData

try:
    from unittest.mock import AsyncMock
except ImportError:
    from asynctest import CoroutineMock as AsyncMock


class TestSsllabs:

    API_CALLS = [("analyze.Analyze",
                  HostData,
                  {
                      "host": "devolo.de"
                  }),
                 ("info.Info",
                  InfoData,
                  {}),
                 ("status_codes.StatusCodes",
                  StatusCodesData,
                  {})]

    @pytest.mark.asyncio
    @pytest.mark.parametrize("api, result, parameters", API_CALLS)
    async def test_ssllabs(self, request, api, result, parameters):
        call = api.split(".")[0]
        with patch(f"ssllabs.api.{api}.get",
                   new=AsyncMock(return_value=from_dict(data_class=result,
                                                        data=getattr(request.cls,
                                                                     call)))):
            ssllabs = Ssllabs()
            api_data = await getattr(ssllabs, call)(**parameters)
            assert dataclasses.asdict(api_data) == getattr(request.cls, call)

    @pytest.mark.asyncio
    async def test_analyze_not_ready_yet(self, request, mocker):
        with patch("asyncio.sleep", new=AsyncMock()), \
             patch("ssllabs.api.analyze.Analyze.get",
                   new=AsyncMock(side_effect=[
                       from_dict(data_class=HostData,
                                 data=request.cls.analyze_running),
                       from_dict(data_class=HostData,
                                 data=request.cls.analyze)
                   ])):
            spy = mocker.spy(Analyze, "get")
            ssllabs = Ssllabs()
            await ssllabs.analyze(host="devolo.de")
            assert spy.call_count == 2

    @pytest.mark.asyncio
    async def test_root_certs(self, request):
        with patch("ssllabs.api.root_certs_raw.RootCertsRaw.get",
                   new=AsyncMock(return_value=request.cls.root_certs["rootCerts"])):
            ssllabs = Ssllabs()
            root_certs = await ssllabs.root_certs()
            assert root_certs == request.cls.root_certs["rootCerts"]

    @pytest.mark.asyncio
    async def test_root_certs_value_error(self):
        with pytest.raises(ValueError):
            ssllabs = Ssllabs()
            await ssllabs.root_certs(trust_store=6)

    @pytest.mark.asyncio
    async def test_availability(self, request):
        with patch("ssllabs.api.info.Info.get",
                   new=AsyncMock(return_Value=from_dict(data_class=InfoData,
                                                        data=request.cls.info))):
            ssllabs = Ssllabs()
            assert await ssllabs.availability()

    @pytest.mark.asyncio
    async def test_availability_http_error(self):
        from httpx import Request, Response
        req = Request("GET", "")
        with patch("httpx._client.AsyncClient.get", new=AsyncMock(return_value=Response(401, request=req))):
            ssllabs = Ssllabs()
            assert not await ssllabs.availability()
