from dataclasses import dataclass
from typing import List

from .simulation import Simulation


@dataclass
class SimDetails:
    """Dataclass for Simulation object lists.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#simdetails
    """

    results: List[Simulation]
    """Instances of Simulation."""
