from dacite import from_dict

from ..data.endpoint import EndpointData
from ._api import _Api


class Endpoint(_Api):
    """Retrieve detailed endpoint information.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#retrieve-detailed-endpoint-information
    """

    async def get(self, host: str, s: str, **kwargs) -> EndpointData:
        """Retrieve detailed endpoint information.

        :param host: Hostname to analyze
        :param s: Endpoint IP address
        :keyword fromCache: Always deliver cached assessment reports if available; optional, defaults to "off". This parameter
                            is intended for API consumers that don't want to wait for assessment results. Can't be used at the
                            same time as the startNew parameter.
        :raises httpx.ConnectTimeout: SSL Labs Servers don't respond.
        :raises httpx.HTTPStatusError: A client or server error response occured.
        :raises httpx.ReadTimeout: SSL Labs Servers don't respond.
        """
        self._verify_kwargs(kwargs.keys(), ["fromCache"])
        r = await self._call("getEndpointData", host=host, s=s, **kwargs)
        return from_dict(data_class=EndpointData, data=r.json())
