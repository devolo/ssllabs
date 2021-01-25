from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class HstsPolicyData:
    """Dataclass for HSTS Policy objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#hstspolicy
    """

    LONG_MAX_AGE: int
    """This constant contains what SSL Labs considers to be sufficiently large max-age value"""

    header: Optional[str]
    """The contents of the HSTS response header, if present"""

    status: str
    """HSTS status"""

    error: Optional[str]
    """Error message when error is encountered, null otherwise"""

    maxAge: Optional[int]
    """The max-age value specified in the policy; null if policy is missing or invalid or on parsing error"""

    includeSubDomains: Optional[bool]
    """True if the includeSubDomains directive is set; null otherwise"""

    preload: Optional[bool]
    """True if the preload directive is set; null otherwise"""

    directives: Optional[Dict]
    """List of raw policy directives"""
