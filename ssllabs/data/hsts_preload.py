from dataclasses import dataclass
from typing import Optional


@dataclass
class HstsPreloadData:
    """Dataclass for HSTS Preload objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#hstspreload
    """

    source: str
    """Source name"""

    hostname: str
    """Name of the host"""

    status: str
    """preload status"""

    error: Optional[str]
    """Error message, when status is 'error'"""

    sourceTime: int
    """Time, as a Unix timestamp, when the preload database was retrieved"""
