from dacite import from_dict

from ..data.info import InfoData
from ._api import _Api


class Info(_Api):
    """General information about the ssllabs API.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#check-ssl-labs-availability
    """

    async def get(self) -> InfoData:
        """Get information."""
        r = await self._call("info")
        return from_dict(data_class=InfoData, data=r.json())
