from dataclasses import dataclass
from typing import Optional


@dataclass
class SimClientData:
    """Dataclass for Simulation Client objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#simclient
    """

    id: int
    """Unique client ID."""

    name: str
    """Name of the client (e.g., Chrome)."""

    platform: Optional[str]
    """Name of the platform (e.g., XP SP3)."""

    version: str
    """Version of the software being simulated (e.g., 49)"""

    isReference: bool
    """
    True if the browser is considered representative of modern browsers, false otherwise. This flag does not correlate to
    client's capabilities, but is used by SSL Labs to determine if a particular configuration is effective. For example, to
    track Forward Secrecy support, we mark several representative browsers as "modern" and then test to see if they succeed in
    negotiating a FS suite. Just as an illustration, modern browsers are currently Chrome, Firefox (not ESR versions),
    IE/Win7, and Safari.
    """
