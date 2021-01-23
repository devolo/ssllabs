from dataclasses import dataclass
from typing import Optional

from .sim_client import SimClient


@dataclass
class Simulation:
    """Dataclass for Simulation objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#simulation
    """

    client: SimClient
    """Instance of SimClient."""

    errorCode: int
    """Zero if handshake was successful, 1 if it was not."""

    errorMessage: Optional[str]
    """Error message if simulation has failed."""

    attempts: int
    """Always 1 with the current implementation."""

    certChainId: int
    """ID of the certificate chain."""

    protocolId: int
    """Negotiated protocol ID."""

    suiteId: int
    """Negotiated suite ID."""

    suiteName: str
    """Negotiated suite Name."""

    kxType: str
    """Negotiated key exchange, for example 'ECDH'."""

    kxStrength: int
    """Negotiated key exchange strength, in RSA-equivalent bits."""

    dhBits: int
    """Strength of DH params (e.g., 1024)"""

    dhP: str
    """DH params, p component"""

    dhG: str
    """DH params, g component"""

    dhYs: str
    """DH params, Ys component"""

    namedGroupBits: Optional[int]
    """When ECDHE is negotiated, length of EC parameters."""

    namedGroupId: Optional[int]
    """When ECDHE is negotiated, EC curve ID."""

    namedGroupName: Optional[str]
    """When ECDHE is negotiated, EC curve nanme (e.g., 'secp256r1')."""

    keyAlg: str
    """Connection certificate key algorithsm (e.g., 'RSA')."""

    keySize: int
    """Connection certificate key size (e.g., 2048)."""

    sigAlg: str
    """Connection certificate signature algorithm (e.g, 'SHA256withRSA')."""
