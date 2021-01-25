from dataclasses import dataclass
from typing import List, Optional

from .trust import TrustData


@dataclass
class TrustPathData:
    """Dataclass for trust path objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#trustpath
    """

    certIds: List[str]
    """List of certificate ID from leaf to root."""

    trust: List[TrustData]
    """Trust object. This object shows info about the trusted certificate by using Mozilla trust store."""

    isPinned: Optional[bool]
    """True if a key is pinned, else false"""

    matchedPins: Optional[int]
    """Number of matched pins with HPKP policy"""

    unmatchedPins: Optional[int]
    """Number of unmatched pins with HPKP policy"""
