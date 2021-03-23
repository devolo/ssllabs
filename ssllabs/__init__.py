from pkg_resources import DistributionNotFound, get_distribution

from .ssllabs import Ssllabs

__license__ = "MIT"

try:
    __version__ = get_distribution(__package__).version
except DistributionNotFound:
    # package is not installed
    __version__ = "0.0.0"

__all__ = ['Ssllabs', "__license__", "__version__"]
