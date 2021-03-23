from .ssllabs import Ssllabs

try:
    from importlib.metadata import PackageNotFoundError, version
except ImportError:
    from importlib_metadata import PackageNotFoundError, version  # type: ignore[no-redef]

__license__ = "MIT"

try:
    __version__ = version("package-name")
except PackageNotFoundError:
    # package is not installed - e.g. pulled and run locally
    __version__ = "0.0.0"

__all__ = ['Ssllabs', "__license__", "__version__"]
