from ._api import _Api


class RootCertsRaw(_Api):
    """Retrieve root certificates.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#retrieve-root-certificates
    """

    async def get(self, **kwargs) -> str:
        """Retrieve root certificates.

        :keyword trustStore: 1-Mozilla(default), 2-Apple MacOS, 3-Android, 4-Java, 5-Windows
        :raises httpx.ConnectTimeout: SSL Labs Servers don't respond.
        :raises httpx.HTTPStatusError: A client or server error response occured.
        :raises httpx.ReadTimeout: SSL Labs Servers don't respond.
        """
        self._verify_kwargs(kwargs.keys(), ["trustStore"])
        r = await self._call("getRootCertsRaw", **kwargs)
        return r.text
