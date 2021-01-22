from ..data.status_codes import StatusCodesData
from ._api import _Api


class StatusCodes(_Api):
    """Retrieve known status codes.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#retrieve-known-status-codes
    """

    async def get(self) -> StatusCodesData:
        """Retrieve known status codes."""
        r = await self._call("getStatusCodes")
        return StatusCodesData(**r.json())
