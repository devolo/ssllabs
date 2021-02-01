import asyncio
import json
import os
import pathlib
from unittest.mock import patch

import pytest
from httpx import Response

try:
    from unittest.mock import AsyncMock
except ImportError:
    from asynctest import CoroutineMock as AsyncMock


@pytest.fixture(autouse=True, scope="class")
def test_data_fixture(request):
    """ Load test data. """
    path = pathlib.Path(__file__).parent / "test_data"
    files = list(path.glob("*.json"))
    for file in files:
        filename = os.path.splitext(file.name)[0]
        with file.open("r") as fh:
            test_data = json.load(fh)
            setattr(request.cls, filename, test_data)


@pytest.fixture()
def patch_httpx():
    with patch('ssllabs.api._api._Api._call', new=AsyncMock(return_value=Response(200))) as r:
        yield r


@pytest.fixture
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.run_until_complete(
        asyncio.tasks.gather(*[task.cancel() for task in asyncio.tasks.all_tasks(loop)],
                             return_exceptions=True))
    loop.close()
