from .ssllabs import Ssllabs

__all__ = ['Ssllabs']
__version__ = "0.1.0"

__locals = locals()

for _name in __all__:
    if not _name.startswith("__"):
        setattr(__locals[_name], "__module__", "ssllabs")
