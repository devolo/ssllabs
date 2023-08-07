import asyncio
import logging
from typing import Optional

from httpx import AsyncClient, ConnectTimeout, HTTPStatusError, ReadError, ReadTimeout

from .api import Analyze, Info, RootCertsRaw, StatusCodes
from .data.host import HostData
from .data.info import InfoData
from .data.status_codes import StatusCodesData


class Ssllabs:
    """Highlevel methods to interact with the SSL Labs Assessment APIs."""

    def __init__(self, client: Optional[AsyncClient] = None):
        self._client = client
        self._logger = logging.getLogger("ssllabs.Ssllabs")
        self._semaphore = asyncio.Semaphore(1)

    async def availability(self) -> bool:
        """
        Check the availability of the SSL Labs servers.

        See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#error-response-status-codes
        """
        i = Info(self._client)
        try:
            await i.get()
            self._logger.info("SSL Labs servers are up an running.")
            return True
        except (HTTPStatusError, ReadError, ReadTimeout, ConnectTimeout) as ex:
            self._logger.error(ex)
            return False

    async def analyze(
        self,
        host: str,
        publish: bool = False,
        ignore_mismatch: bool = False,
        from_cache: bool = False,
        max_age: Optional[int] = None,
    ) -> HostData:
        """
        Test a particular host with respect to the cool off and the maximum number of assessments.

        :param host: Host to test
        :param publish: True if assessment results should be published on the public results boards
        :param ignore_mismatch: True if assessment shall proceed even when the server certificate doesn't match the hostname
        :param from_cache: True if cached results should be used instead of new assessments
        :param max_age: Maximum age cached data might have in hours

        See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#protocol-usage
        """
        await self._semaphore.acquire()
        self._logger.info("Analyzing %s", host)
        i = Info(self._client)
        info = await i.get()

        # Wait for a free slot, if all slots are in use
        while info.currentAssessments >= info.maxAssessments:
            self._logger.warning("Already %i assessments running. Need to wait.", info.currentAssessments)
            await asyncio.sleep(1)
            info = await i.get()

        # If there is already an assessment running, wait the needed cool off until starting the next one
        if info.currentAssessments != 0:
            await asyncio.sleep(info.newAssessmentCoolOff / 1000)

        a = Analyze(self._client)
        host_object = await a.get(
            host=host,
            startNew="off" if from_cache else "on",
            fromCache="on" if from_cache else "off",
            publish="on" if publish else "off",
            ignoreMismatch="on" if ignore_mismatch else "off",
            maxAge=max_age,
        )
        self._semaphore.release()
        while host_object.status not in ["READY", "ERROR"]:
            self._logger.debug("Assessment of %s not ready yet.", host)
            await asyncio.sleep(10)
            host_object = await a.get(host=host, all="done")
        return host_object

    async def info(self) -> InfoData:
        """
        Retrieve the engine and criteria version, and initialize the maximum number of concurrent assessments.

        See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#info
        """
        i = Info(self._client)
        return await i.get()

    async def root_certs(self, trust_store: int = 1) -> str:
        """
        Retrieve root certificates.

        :param trust_store: Trust store to return (1-Mozilla, 2-Apple MacOS, 3-Android, 4-Java, 5-Windows)

        See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#retrieve-root-certificates
        """
        if not 1 <= trust_store <= 5:
            raise ValueError(
                """Trust store not found. Please choose on of the following:
            1-Mozilla, 2-Apple MacOS, 3-Android, 4-Java, 5-Windows"""
            )
        rcr = RootCertsRaw(self._client)
        return await rcr.get(trustStore=trust_store)

    async def status_codes(self) -> StatusCodesData:
        """
        Retrieve known status codes.

        See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#retrieve-known-status-codes
        """
        sc = StatusCodes(self._client)
        return await sc.get()
