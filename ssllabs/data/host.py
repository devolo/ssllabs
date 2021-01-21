from dataclasses import dataclass
from typing import List

from .endpoint import EndpointData


@dataclass
class HostData:
    """Dataclass for host objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#host
    """

    host: str
    port: int
    protocol: str
    isPublic: bool
    status: str
    startTime: int
    testTime: int
    engineVersion: str
    criteriaVersion: str
    cacheExpiryTime: str
    certHostnames: List[str]
    endpoints: List[EndpointData]
    # certs: List[CertData]
