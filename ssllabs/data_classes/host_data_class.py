from dataclasses import *
from typing import List

from .endpoint_data_class import EndpointDataClass


@dataclass
class HostDataClass:
    host: str
    port: int
    protocol: str
    isPublic: bool
    status: str
    startTime: int
    testTime: int
    engineVersion: str
    criteriaVersion: str
    endpoints: List[EndpointDataClass]