from dataclasses import dataclass


@dataclass
class StatusCodesData:
    """Dataclass for StatusCodes instances.

    See also: https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#statuscodes
    """

    # ToDo: Check typing
    statusDetails: str
    """
    A map containing all status details codes and the corresponding English translations. Please note that, once in use, the
    codes will not change, whereas the translations may change at any time.
    """
