"""Qualys SSL Labs API in Python."""
try:
    from importlib.metadata import PackageNotFoundError, version
except ImportError:
    from importlib_metadata import PackageNotFoundError, version  # type: ignore

from .ssllabs import Ssllabs

__license__ = "MIT"

try:
    __version__ = version("ssllabs")
except PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0"

__all__ = ["Ssllabs", "__license__", "__version__"]
