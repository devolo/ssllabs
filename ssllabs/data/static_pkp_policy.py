from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class StaticPkpPolicyData:
    """Dataclass for SPKP Policy objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#staticpkppolicy
    """

    status: str
    """SPKP status"""

    error: Optional[str]
    """Error message, when the policy is invalid"""

    includeSubDomains: Optional[bool]
    """True if the includeSubDomains directive is set else false"""

    reportUri: Optional[str]
    """The report-uri value from the policy"""

    pins: List[Dict]
    """List of all pins used by the policy"""

    matchedPins: List[Dict]
    """List of pins that match the current configuration"""

    forbiddenPins: List[Dict]
    """List of all forbidden pins used by policy"""

    matchedForbiddenPins: List[Dict]
    """List of forbidden pins that match the current configuration"""
