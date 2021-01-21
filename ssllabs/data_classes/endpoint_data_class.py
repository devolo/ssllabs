from dataclasses import *
from typing import List


@dataclass
class EndpointDataClass:
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
    # details
    