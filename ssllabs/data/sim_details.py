from dataclasses import dataclass
from typing import List

from .simulation import SimulationData


@dataclass
class SimDetailsData:
    """Dataclass for Simulation object lists.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#simdetails
    """

    results: List[SimulationData]
    """Instances of Simulation."""
