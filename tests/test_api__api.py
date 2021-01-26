from unittest.mock import patch

import pytest

from ssllabs.api._api import _Api

try:
    from unittest.mock import AsyncMock
except ImportError:
    from asynctest import CoroutineMock as AsyncMock
from httpx import Response
