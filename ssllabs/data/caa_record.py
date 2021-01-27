from dataclasses import dataclass


@dataclass
class CaaRecordData:
    """Dataclass for CAA Record objects.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#caarecord
    """

    tag: str
    """A property of the CAA record"""

    value: str
    """Corresponding value of a CAA property"""

    flags: int
    """Corresponding flags of CAA property (8 bit)"""
