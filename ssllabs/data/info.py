from dataclasses import dataclass
from typing import List


@dataclass
class InfoData:
    """Dataclass for info objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#info
    """
    engineVersion: str
    criteriaVersion: str
    maxAssessments: int
    currentAssessments: int
    newAssessmentCoolOff: int
    messages: List[str]
