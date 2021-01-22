from dataclasses import dataclass
from typing import Dict


@dataclass
class StatusCodesData:
    """Dataclass for StatusCodes instances.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#statuscodes
    """

    statusDetails: Dict
    """
    A map containing all status details codes and the corresponding English translations. Please note that, once in use, the
    codes will not change, whereas the translations may change at any time.
    """
