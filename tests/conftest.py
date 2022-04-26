import asyncio
import json
import os
import pathlib

import pytest


@pytest.fixture(autouse=True, scope="class")
def test_data_fixture(request):
    """Load test data."""
    path = pathlib.Path(__file__).parent / "test_data"
    files = list(path.glob("*.json"))
    for file in files:
        filename = os.path.splitext(file.name)[0]
        with file.open("r") as fh:
            test_data = json.load(fh)
            setattr(request.cls, filename, test_data)


@pytest.fixture()
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    to_cancel = asyncio.tasks.all_tasks(loop)
    for task in to_cancel:
        task.cancel()
    loop.run_until_complete(asyncio.tasks.gather(*to_cancel, return_exceptions=True))
    loop.close()
