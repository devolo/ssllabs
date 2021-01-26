from dataclasses import dataclass
from typing import Optional

from .sim_client import SimClientData


@dataclass
class SimulationData:
    """Dataclass for Simulation objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#simulation
    """

    client: SimClientData
    """Instance of SimClient."""

    errorCode: int
    """Zero if handshake was successful, 1 if it was not."""

    errorMessage: Optional[str]
    """Error message if simulation has failed."""

    attempts: int
    """Always 1 with the current implementation."""

    certChainId: Optional[str]
    """ID of the certificate chain."""

    protocolId: Optional[int]
    """Negotiated protocol ID."""

    suiteId: Optional[int]
    """Negotiated suite ID."""

    suiteName: Optional[str]
    """Negotiated suite Name."""

    kxType: Optional[str]
    """Negotiated key exchange, for example 'ECDH'."""

    kxStrength: Optional[int]
    """Negotiated key exchange strength, in RSA-equivalent bits."""

    dhBits: Optional[int]
    """Strength of DH params (e.g., 1024)"""

    dhP: Optional[int]
    """DH params, p component"""

    dhG: Optional[int]
    """DH params, g component"""

    dhYs: Optional[int]
    """DH params, Ys component"""

    namedGroupBits: Optional[int]
    """When ECDHE is negotiated, length of EC parameters."""

    namedGroupId: Optional[int]
    """When ECDHE is negotiated, EC curve ID."""

    namedGroupName: Optional[str]
    """When ECDHE is negotiated, EC curve nanme (e.g., 'secp256r1')."""

    keyAlg: Optional[str]
    """Connection certificate key algorithsm (e.g., 'RSA')."""

    keySize: Optional[int]
    """Connection certificate key size (e.g., 2048)."""

    sigAlg: Optional[str]
    """Connection certificate signature algorithm (e.g, 'SHA256withRSA')."""
