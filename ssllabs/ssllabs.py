import asyncio
import logging

from httpx import HTTPStatusError

from .api.analyze import Analyze
from .api.info import Info
from .api.root_certs_raw import RootCertsRaw
from .api.status_codes import StatusCodes
from .data.host import HostData
from .data.info import InfoData
from .data.status_codes import StatusCodesData


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

    async def analyze(self, host: str, publish: bool = False, ignore_mismatch: bool = False) -> HostData:
        """
        Test a particular host.

        :param host: Host to test
        :param publish: True if assessment results should be published on the public results boards
        :param ignore_mismatch: True if assessment shall proceed even when the server certificate doesn't match the hostname

        See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#protocol-usage
        """
        api = Analyze()
        publish = publish == "on"
        igonreMismatch = ignore_mismatch == "on"
        host_object = await api.get(host=host, startNew="on", publish=publish, igonreMismatch=igonreMismatch)
        while host_object.status not in ["READY", "ERROR"]:
            self.logger.debug("Analyzing %s", host)
            await asyncio.sleep(10)
            host_object = await api.get(host=host, all="done")
        return host_object

    async def info(self) -> InfoData:
        """
        Retrieve the engine and criteria version, and initialize the maximum number of concurrent assessments.

        See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#info
        """
        api = Info()
        return await api.get()

    async def root_certs(self, trust_store: int = 1) -> str:
        """
        Retrieve root certificates.

        :param trust_store: Trust store to return (1-Mozilla, 2-Apple MacOS, 3-Android, 4-Java, 5-Windows)

        See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#retrieve-root-certificates
        """
        if not 1 <= trust_store <= 5:
            raise ValueError("""Trust store not found. Please choose on of the following:
            1-Mozilla, 2-Apple MacOS, 3-Android, 4-Java, 5-Windows""")
        api = RootCertsRaw()
        return await api.get(trustStore=trust_store)

    async def status_codes(self) -> StatusCodesData:
        """
        Retrieve known status codes.

        See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#retrieve-known-status-codes
        """
        api = StatusCodes()
        return await api.get()
