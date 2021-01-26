from dataclasses import dataclass
from typing import List, Optional

from .named_group import NamedGroupData


@dataclass
class NamedGroupsData:
    """Dataclass for NamedGroup object lists.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#namedgroups
    """

    list: List[NamedGroupData]
    """An array of NamedGroup objects"""

    preference: Optional[bool]
    """True if the server has preferred curves that it uses first"""
