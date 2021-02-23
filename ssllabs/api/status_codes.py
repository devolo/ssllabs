from dacite import from_dict

from ..data.status_codes import StatusCodesData
from ._api import _Api


class StatusCodes(_Api):
    """Retrieve known status codes.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#retrieve-known-status-codes
    """

    async def get(self) -> StatusCodesData:
        """Retrieve known status codes.

        :raises httpx.ConnectTimeout: SSL Labs Servers don't respond.
        :raises httpx.HTTPStatusError: A client or server error response occured.
        :raises httpx.ReadTimeout: SSL Labs Servers don't respond.
        """
        r = await self._call("getStatusCodes")
        return from_dict(data_class=StatusCodesData, data=r.json())
