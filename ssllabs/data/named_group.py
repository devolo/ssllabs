from dataclasses import dataclass


@dataclass
class NamedGroupData:
    """Dataclass for NamedGroup objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#namedgroup
    """

    id: int
    """Named curve ID"""

    name: str
    """named curve name"""

    bits: int
    """Named curve strength in EC bits"""
