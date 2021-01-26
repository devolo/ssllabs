from dataclasses import dataclass
from typing import List, Optional

from .cert import CertData
from .endpoint import EndpointData


@dataclass
class HostData:
    """Dataclass for host objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#host
    """

    host: str
    """Assessment host, which can be a hostname or an IP address"""

    port: int
    """Assessment port (e.g., 443)"""

    protocol: str
    """Protocol (e.g., HTTP)"""

    isPublic: bool
    """True if this assessment is publicly available (listed on the SSL Labs assessment boards)"""

    status: str
    """Assessment status; possible values: DNS, ERROR, IN_PROGRESS, and READY."""

    statusMessage: Optional[str]
    """Status message in English. When status is ERROR, this field will contain an error message."""

    startTime: int
    """Assessment starting time, in milliseconds since 1970"""

    testTime: Optional[int]
    """Assessment completion time, in milliseconds since 1970"""

    engineVersion: str
    """Assessment engine version (e.g., '1.26.5')"""

    criteriaVersion: str
    """Grading criteria version (e.g., '2009l')"""

    cacheExpiryTime: Optional[int]
    """
    When will the assessment results expire from the cache (typically set only for assessment with errors; otherwise the
    results stay in the cache for as long as there's sufficient room)
    """

    certHostnames: Optional[List[str]]
    """
    The list of certificate hostnames collected from the certificates seen during assessment. The hostnames may not be valid.
    This field is available only if the server certificate doesn't match the requested hostname. In that case, this field
    saves you some time as you don't have to inspect the certificates yourself to find out what valid hostnames might be.
    """

    endpoints: Optional[List[EndpointData]]
    """List of Endpoint objects"""

    certs: Optional[List[CertData]]
    """
    A list of Cert object, representing the chain certificates in the order in which they were retrieved from the server.
    """
