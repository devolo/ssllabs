from dataclasses import dataclass
# from typing import List


@dataclass
class EndpointData:
    """Dataclass for endpoint objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#endpoint
    """

    ipAddress: str
    serverName: str
    statusMessage: str
    grade: str
    gradeTrustIgnored: str
    hasWarnings: bool
    isExceptional: bool
    progress: int
    duration: int
    delegation: int
    # details: List[EndpointDetailsData]  # This is just a reminder
