from dataclasses import dataclass
from typing import List, Optional

from .suite import SuiteData


@dataclass
class ProtocolSuitesData:
    """Dataclass for protocol suites objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#protocolsuites
    """

    protocol: int
    """Protocol version."""

    list: List[SuiteData]
    """List of Suite objects"""

    preference: Optional[bool]
    """
    True if the server actively selects cipher suites; if null, we were not able to determine if the server has a preference
    """

    chaCha20Preference: Optional[bool]
    """
    True if the server takes into account client preferences when deciding if to use ChaCha20 suites. null, we were not able
    to determine if the server has a chacha preference.
    """
