import json
import os
import pathlib

import pytest


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
