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


# ToDo: test_analyze, test_info, and test_status_codes can be combined with parametrize
class TestSsllabs:

    @pytest.mark.asyncio
    async def test_analyze(self, request):
        with patch("ssllabs.api.analyze.Analyze.get",
                   new=AsyncMock(return_value=from_dict(data_class=HostData,
                                                        data=request.cls.analyze))):
            ssllabs = Ssllabs()
            analyze = await ssllabs.analyze(host="devolo.de")
            assert dataclasses.asdict(analyze) == request.cls.analyze

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
    async def test_info(self, request):
        with patch("ssllabs.api.info.Info.get",
                   new=AsyncMock(return_value=from_dict(data_class=InfoData,
                                                        data=request.cls.info))):
            ssllabs = Ssllabs()
            info = await ssllabs.info()
            assert dataclasses.asdict(info) == request.cls.info

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
    async def test_status_codes(self, request):
        with patch("ssllabs.api.status_codes.StatusCodes.get",
                   new=AsyncMock(return_value=from_dict(data_class=StatusCodesData,
                                                        data=request.cls.status_codes))):
            ssllabs = Ssllabs()
            status_codes = await ssllabs.status_codes()
            assert dataclasses.asdict(status_codes) == request.cls.status_codes

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
