from dataclasses import dataclass
from typing import Optional


@dataclass
class TrustData:
    """Dataclass for trust objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#trust
    """

    rootStore: str
    """this field shows the Trust store being used (eg. 'Mozilla')"""

    isTrusted: Optional[bool]
    """True if trusted against above rootStore"""

    trustErrorMessage: Optional[str]
    """Shows the error message if any"""
