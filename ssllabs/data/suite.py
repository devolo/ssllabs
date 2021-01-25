from dataclasses import dataclass
from typing import Optional


@dataclass
class SuiteData:
    """Dataclass for suite objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#suite
    """

    id: int
    """Suite RFC ID"""

    name: str
    """Suite name (e.g., TLS_RSA_WITH_RC4_128_SHA)"""

    cipherStrength: int
    """Suite strength (e.g., 128)"""

    kxType: str
    """Key exchange type (e.g., ECDH)"""

    kxStrength: int
    """Key exchange strength, in RSA-equivalent bits"""

    dhP: Optional[str]
    """DH params, p component"""

    dhG: Optional[str]
    """DH params, g component"""

    dhYs: Optional[str]
    """DH params, Ys component"""

    namedGroupBits: int
    """EC bits"""

    namedGroupId: int
    """EC curve ID"""

    namedGroupName: str
    """EC curve name"""

    q: Optional[int]
    """Flag for suite insecure or weak. Not present if suite is strong or good"""
