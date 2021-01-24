from unittest.mock import patch

import pytest
from dacite import from_dict

from ssllabs.data.status_codes import StatusCodesData
from ssllabs.ssllabs import Ssllabs


class TestSsllabs:

    @pytest.mark.asyncio
    async def test_status_codes(self, request):
        with patch("ssllabs.api.status_codes.StatusCodes.get",
                   return_value=from_dict(data_class=StatusCodesData, data=request.cls.status_details)):
            ssllabs = Ssllabs()
            status_codes = await ssllabs.status_codes()
            assert status_codes.statusDetails == request.cls.status_details["statusDetails"]
