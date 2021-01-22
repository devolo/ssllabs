from dacite import from_dict

from ..data.endpoint import EndpointData
from ._api import _Api


class Endpoint(_Api):
    """Retrieve detailed endpoint information.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#retrieve-detailed-endpoint-information
    """
    async def get(self, host: str, endpoint_ip: str, **kwargs) -> EndpointData:
        """Retrieve detailed endpoint information.

        :param host: Hostname to analyze
        :param endpoint_ip: Endpoint IP address
        :key fromCache: Always deliver cached assessment reports if available; optional, defaults to "off". This parameter is
                        intended for API consumers that don't want to wait for assessment results. Can't be used at the same
                        time as the startNew parameter.
        """
        r = await self._call("getEndpointData",
                             host=host,
                             s=endpoint_ip,
                             **kwargs)
        return from_dict(data_class=EndpointData, data=r.json())
