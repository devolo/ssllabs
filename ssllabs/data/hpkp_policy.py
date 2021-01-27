from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class HpkpPolicyData:
    """Dataclass for HPKP Policy objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#hpkppolicy
    """

    header: Optional[str]
    """The contents of the HPKP response header, if present"""

    status: str
    """HPKP status"""

    error: Optional[str]
    """Error message, when the policy is invalid"""

    maxAge: Optional[int]
    """The max-age value from the policy"""

    includeSubDomains: Optional[bool]
    """True if the includeSubDomains directive is set; null otherwise"""

    reportUri: Optional[str]
    """The report-uri value from the policy"""

    pins: List[Dict]
    """List of all pins used by the policy"""

    matchedPins: List[Dict]
    """List of pins that match the current configuration"""

    directives: List[Dict]
    """List of raw policy directives (name-value pairs)"""
