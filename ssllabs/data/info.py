from dataclasses import dataclass
from typing import List


@dataclass
class InfoData:
    """Dataclass for info objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#info
    """

    engineVersion: str
    """SSL Labs software version as a string (e.g., '1.11.14')"""

    criteriaVersion: str
    """Rating criteria version as a string (e.g., '2009f')"""

    maxAssessments: int
    """The maximum number of concurrent assessments the client is allowed to initiate."""

    currentAssessments: int
    """The number of ongoing assessments submitted by this client."""

    newAssessmentCoolOff: int
    """
    The cool-off period after each new assessment, in milliseconds; you're not allowed to submit a new assessment before
    the cool-off expires, otherwise you'll get a 429.
    """

    messages: List[str]
    """
    A list of messages (strings). Messages can be public (sent to everyone) and private (sent only to the invoking client).
    Private messages are prefixed with '[Private]'.
    """
