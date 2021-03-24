from dacite import from_dict

from ..data.host import HostData
from ._api import _Api


class Analyze(_Api):
    """Invoke assessment and check progress.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#invoke-assessment-and-check-progress
    """

    async def get(self, host: str, **kwargs) -> HostData:
        """Analyze host.

        :param host: Hostname to analyze
        :keyword publish: Set to "on" if assessment results should be published on the public results boards; optional,
                          defaults to "off".
        :keyword startNew: If set to "on" then cached assessment results are ignored and a new assessment is started. However,
                           if there's already an assessment in progress, its status is delivered instead. This parameter
                           should be used only once to initiate a new assessment; further invocations should omit it to avoid
                           causing an assessment loop.
        :keyword fromCache: Always deliver cached assessment reports if available; optional, defaults to "off". This parameter
                            is intended for API consumers that don't want to wait for assessment results. Can't be used at the
                            same time as the startNew parameter.
        :keyword maxAge: Maximum report age, in hours, if retrieving from cache (fromCache parameter set).
        :keyword all: By default this call results only summaries of individual endpoints. If this parameter is set to "on",
                      full information will be returned. If set to "done", full information will be returned only if the
                      assessment is complete (status is READY or ERROR).
        :keyword ignoreMismatch: Set to "on" to proceed with assessments even when the server certificate doesn't match the
                                 assessment hostname. Set to off by default. Please note that this parameter is ignored if a
                                 cached report is returned.
        :raises httpx.ConnectTimeout: SSL Labs Servers don't respond.
        :raises httpx.HTTPStatusError: A client or server error response occured.
        :raises httpx.ReadTimeout: SSL Labs Servers don't respond.
        """
        self._verify_kwargs(kwargs.keys(), ["publish", "startNew", "fromCache", "maxAge", "all", "ignoreMismatch"])
        r = await self._call("analyze", host=host, **kwargs)
        return from_dict(data_class=HostData, data=r.json())
