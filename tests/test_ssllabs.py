import asyncio
import dataclasses
from unittest.mock import patch

import pytest
from dacite import from_dict
from httpx import ConnectTimeout, HTTPStatusError, ReadError, ReadTimeout, TransportError

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
    API_CALLS: list = [("info.Info", InfoData, {}), ("status_codes.StatusCodes", StatusCodesData, {})]

    @pytest.mark.asyncio
    @pytest.mark.parametrize("api, result, parameters", API_CALLS)
    async def test_ssllabs(self, request, api, result, parameters):
        call = api.split(".")[0]
        with patch(
            f"ssllabs.api.{api}.get", new=AsyncMock(return_value=from_dict(data_class=result, data=getattr(request.cls, call)))
        ):
            ssllabs = Ssllabs()
            api_data = await getattr(ssllabs, call)(**parameters)
            assert dataclasses.asdict(api_data) == getattr(request.cls, call)

    @pytest.mark.asyncio
    async def test_analyze(self, request: pytest.FixtureRequest) -> None:
        with patch(
            "ssllabs.api.info.Info.get", new=AsyncMock(return_value=from_dict(data_class=InfoData, data=request.cls.info))
        ), patch(
            "ssllabs.api.analyze.Analyze.get",
            new=AsyncMock(return_value=from_dict(data_class=HostData, data=request.cls.analyze)),
        ) as get:
            ssllabs = Ssllabs()
            api_data = await ssllabs.analyze(host="devolo.de")
            assert dataclasses.asdict(api_data) == request.cls.analyze
            get.assert_called_with(
                host="devolo.de", ignoreMismatch="off", publish="off", startNew="on", fromCache="off", maxAge=None, all="done"
            )
            api_data = await ssllabs.analyze(host="devolo.de", from_cache=True, max_age=1)
            assert dataclasses.asdict(api_data) == request.cls.analyze
            get.assert_called_with(
                host="devolo.de", ignoreMismatch="off", publish="off", startNew="off", fromCache="on", maxAge=1, all="done"
            )

    @pytest.mark.asyncio
    async def test_analyze_not_ready_yet(self, request, mocker):
        with patch("asyncio.sleep", new=AsyncMock()), patch(
            "ssllabs.api.info.Info.get", new=AsyncMock(return_value=from_dict(data_class=InfoData, data=request.cls.info))
        ), patch(
            "ssllabs.api.analyze.Analyze.get",
            new=AsyncMock(
                side_effect=[
                    from_dict(data_class=HostData, data=request.cls.analyze_running),
                    from_dict(data_class=HostData, data=request.cls.analyze),
                ]
            ),
        ):
            spy = mocker.spy(Analyze, "get")
            ssllabs = Ssllabs()
            await ssllabs.analyze(host="devolo.de")
            assert spy.call_count == 2

    @pytest.mark.asyncio
    async def test_analyze_max_assessments(self, request, mocker):
        with patch("asyncio.sleep", new=AsyncMock()), patch(
            "ssllabs.api.analyze.Analyze.get",
            new=AsyncMock(return_value=from_dict(data_class=HostData, data=request.cls.analyze)),
        ), patch(
            "ssllabs.api.info.Info.get",
            new=AsyncMock(
                side_effect=[
                    from_dict(data_class=InfoData, data=request.cls.info_max_assessments),
                    from_dict(data_class=InfoData, data=request.cls.info),
                ]
            ),
        ):
            spy = mocker.spy(asyncio, "sleep")
            ssllabs = Ssllabs()
            await ssllabs.analyze(host="devolo.de")
            assert spy.call_count == 1

    @pytest.mark.asyncio
    async def test_analyze_running_assessments(self, request, mocker):
        with patch("asyncio.sleep", new=AsyncMock()), patch(
            "ssllabs.api.analyze.Analyze.get",
            new=AsyncMock(return_value=from_dict(data_class=HostData, data=request.cls.analyze)),
        ), patch(
            "ssllabs.api.info.Info.get",
            new=AsyncMock(return_value=from_dict(data_class=InfoData, data=request.cls.info_running_assessments)),
        ):
            spy = mocker.spy(asyncio, "sleep")
            ssllabs = Ssllabs()
            await ssllabs.analyze(host="devolo.de")
            assert spy.call_count == 1

    @pytest.mark.asyncio
    async def test_root_certs(self, request):
        with patch(
            "ssllabs.api.root_certs_raw.RootCertsRaw.get", new=AsyncMock(return_value=request.cls.root_certs["rootCerts"])
        ):
            ssllabs = Ssllabs()
            root_certs = await ssllabs.root_certs()
            assert root_certs == request.cls.root_certs["rootCerts"]

    @pytest.mark.asyncio
    async def test_root_certs_value_error(self):
        with pytest.raises(ValueError):
            ssllabs = Ssllabs()
            await ssllabs.root_certs(trust_store=6)

    @pytest.mark.asyncio
    async def test_availabile(self, request):
        with patch(
            "ssllabs.api.info.Info.get", new=AsyncMock(return_Value=from_dict(data_class=InfoData, data=request.cls.info))
        ):
            ssllabs = Ssllabs()
            assert await ssllabs.availability()

    @pytest.mark.asyncio
    @pytest.mark.parametrize("exception", [ReadError, ReadTimeout, ConnectTimeout])
    async def test_unavailabile_timeout(self, exception: TransportError) -> None:
        with patch("ssllabs.api.info.Info.get", new=AsyncMock(side_effect=exception(message="", request=""))):
            ssllabs = Ssllabs()
            assert not await ssllabs.availability()

    @pytest.mark.asyncio
    async def test_unavailabile_status_error(self):
        with patch(
            "ssllabs.api.info.Info.get", new=AsyncMock(side_effect=HTTPStatusError(message="", request="", response=""))
        ):
            ssllabs = Ssllabs()
            assert not await ssllabs.availability()
