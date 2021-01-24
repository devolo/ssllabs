import asyncio
import logging

from httpx import HTTPStatusError

from .api.analyze import Analyze
from .api.info import Info
from .data.host import HostData


class Ssllabs():
    """Highlevel methods to interact with the SSL Labs Assessment APIs."""

    def __init__(self):
        self.logger = logging.getLogger(f"{self.__class__.__module__}.{self.__class__.__name__}")

    async def availability(self) -> bool:
        """
        Check the availability of the SSL Labs servers.

        See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#error-response-status-codes
        """
        api = Info()
        try:
            await api.get()
            return True
        except HTTPStatusError as ex:
            self.logger.error(ex)
            return False

    async def analyze(self, host: str) -> HostData:
        """
        Test a particular host.

        See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#protocol-usage
        """
        api = Analyze()
        host_object = await api.get(host=host, startNew="on")
        while host_object.status not in ["READY", "ERROR"]:
            self.logger.debug("Analyzing %s", host)
            await asyncio.sleep(10)
            host_object = await api.get(host=host, all="done")
        return host_object
