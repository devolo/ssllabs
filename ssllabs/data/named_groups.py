from dataclasses import dataclass
from typing import List

from .named_group import NamedGroup


@dataclass
class NamedGroups:
    """Dataclass for NamedGroup object lists.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#namedgroups
    """

    list: List[NamedGroup]
    """An array of NamedGroup objects"""

    preference: bool
    """True if the server has preferred curves that it uses first"""
