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

    kxType: Optional[str]
    """Key exchange type (e.g., ECDH)"""

    kxStrength: Optional[int]
    """Key exchange strength, in RSA-equivalent bits"""

    dhP: Optional[int]
    """DH params, p component"""

    dhG: Optional[int]
    """DH params, g component"""

    dhYs: Optional[int]
    """DH params, Ys component"""

    namedGroupBits: Optional[int]
    """EC bits"""

    namedGroupId: Optional[int]
    """EC curve ID"""

    namedGroupName: Optional[str]
    """EC curve name"""

    q: Optional[int]
    """Flag for suite insecure or weak. Not present if suite is strong or good"""
