from dataclasses import dataclass
from typing import Optional


@dataclass
class ProtocolData:
    """Dataclass for protocol objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#protocol
    """

    id: int
    """Protocol version, e.g. 771 for TLS 1.2 (0x0303)"""

    name: str
    """Protocol name SSL/TLS."""

    version: str
    """Protocol version, e.g. 1.2, 1.1 etc"""

    v2SuitesDisabled: Optional[bool]
    """
    Some servers have SSLv2 protocol enabled, but with all SSLv2 cipher suites disabled. In that case, this field is set to
    True.
    """

    q: Optional[int]
    """0 if the protocol is insecure"""
