# ssllabs Unittests

The unittests are based on pytest.

## System requirements

Defining the system requirements with exact versions typically is difficult. But there is a tested environment:

* Linux
* Python 3.7.9
* pytest 4.5.0
* pytest-asyncio 0.14.0
* pytest-httpx 0.10.1
* pytest-mock 6.2.1
* asynctest 0.13.0

## Running the tests

Install the extra requirements and start pytest.

```bash
pip install -e .[test]
pytest
```
