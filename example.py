"""Get grade of multiple servers."""
import asyncio
import logging
from typing import List

from ssllabs import Ssllabs
from ssllabs.data.host import HostData

HOSTS = [
    "devolo.com",
    "www.devolo.com",
]


async def analyze(hosts: List[str]) -> List[HostData]:
    """Analyze servers."""
    ssllabs = Ssllabs()
    if not await ssllabs.availability():
        raise
    return await asyncio.gather(*[ssllabs.analyze(host=host) for host in hosts])


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s: %(message)s")
    results = asyncio.run(analyze(HOSTS))
    for result in results:
        for endpoint in result.endpoints:
            if endpoint.grade:
                logging.info("Grade of %s (%s): %s", result.host, endpoint.ipAddress, endpoint.grade)
            else:
                logging.error(endpoint.statusMessage)
