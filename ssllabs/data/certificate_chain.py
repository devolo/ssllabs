from dataclasses import dataclass
from typing import List

from .trust_path import TrustPathData


@dataclass
class CertificateChainData:
    """Dataclass for certificate chain objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#certificatechain
    """

    id: str
    """Certificate chain ID"""

    certIds: List[str]
    """
    List of IDs of each certificate, representing the chain certificates in the order in which they were retrieved from the
    server
    """

    trustPaths: List[TrustPathData]
    """Trust path object"""

    issues: int
    """A number of flags that describe the chain and the problems it has."""

    noSni: bool
    """True for certificate obtained only with No Server Name Indication (SNI)."""
