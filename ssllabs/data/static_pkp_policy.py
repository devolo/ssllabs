from dataclasses import dataclass
from typing import List, Optional


@dataclass
class StaticPkpPolicy:
    """Dataclass for SPKP Policy objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#staticpkppolicy
    """

    status: str
    """SPKP status"""

    error: Optional[str]
    """Error message, when the policy is invalid"""

    includeSubDomains: bool
    """True if the includeSubDomains directive is set else false"""

    reportUri: str
    """The report-uri value from the policy"""

    # ToDo: Check datatype of list emelements
    pins: List
    """List of all pins used by the policy"""

    # ToDo: Check datatype of list emelements
    matchedPins: List
    """List of pins that match the current configuration"""

    # ToDo: Check datatype of list emelements
    forbiddenPins: List
    """List of all forbidden pins used by policy"""

    # ToDo: Check datatype of list emelements
    matchedForbiddenPins: List
    """List of forbidden pins that match the current configuration"""
