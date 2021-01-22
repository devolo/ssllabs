from ._api import _Api


class RootCertsRaw(_Api):
    """Retrieve root certificates.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#retrieve-root-certificates
    """
    async def get(self, **kwargs) -> str:
        """Retrieve root certificates.

        :key trustStore: 1-Mozilla(default), 2-Apple MacOS, 3-Android, 4-Java, 5-Windows
        """
        r = await self._call("getRootCertsRaw", **kwargs)
        return r.text
