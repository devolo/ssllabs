from dataclasses import *
from typing import List


@dataclass
class InfoData:
    engineVersion: str
    criteriaVersion: str
    maxAssessments: int
    currentAssessments: int
    newAssessmentCoolOff: int
    messages: List[str]