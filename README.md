# ssllabs

This project implements the [Qualys SSL Labs](https://www.ssllabs.com/ssltest/) API in python. It uses [API version 3](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md). All methods are async.

## System requirements

Defining the system requirements with exact versions typically is difficult. But there is a tested environment:

* Linux
* Python 3.7.9
* pip 20.3.3
* dacite 1.6.0
* httpx 0.16.1

Other versions and even other operating systems might work. Feel free to tell us about your experience. If you want to run our unit tests, you also need:

* pytest 4.5.0
* pytest-asyncio 0.14.0
* pytest-mock 6.2.1
* asynctest 0.13.0

## Versioning

In our versioning we follow [Semantic Versioning](https://semver.org/).

## Installing for usage

The Python Package Index takes care for you. Just use pip.

```bash
pip install ssllabs
```

## Installing for development

First, you need to get the sources.

```bash
git clone git@github.com:devolo/ssllabs.git
```

Then you need to take care of the requirements.

```bash
cd ssllabs
python setup.py install
```

If you want to run out tests, install the extra requirements and start pytest.

```bash
pip install -e .[test]
pytest
```

## High level usage

If you want to cover on the common usage cases, you can use our high level implementations.

### Analyzing a host

```python
import asyncio

from ssllabs import Ssllabs

async def analyze():
    ssllabs = Ssllabs()
    return await ssllabs.analyze(host="devolo.de")

asyncio.run(analyze())
```

This will give you a [Host object](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#host) as dataclass. This call runs quite long as it takes time to run all tests. You probably know that from using the [webinterface](https://www.ssllabs.com/ssltest).

### Check availability of the SSL Labs servers

```python
import asyncio

from ssllabs import Ssllabs

async def availability():
    ssllabs = Ssllabs()
    return await ssllabs.availability()

asyncio.run(availability())
```

This will give you True, if the servers are up and running, otherwise False. It will also report False, if you exeeded your rate limits.

### Retrieve API information

```python
import asyncio

from ssllabs import Ssllabs

async def info():
    ssllabs = Ssllabs()
    return await ssllabs.info()

asyncio.run(info())
```

This will give you an [Info object](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#info) as dataclass.

### Retrieve root certificates

```python
import asyncio

from ssllabs import Ssllabs

async def root_certs():
    ssllabs = Ssllabs()
    return await ssllabs.root_certs(trust_store=1)

asyncio.run(root_certs())
```

This will give you a string containing the latest root certificates used for trust validation. By default it used the certificates provided by Mozilla. You can choose a differenty store by changing trust_store to 1: Mozilla, 2: Apple MacOS, 3: Android, 4: Java or 5: Windows.

### Retrieve known status codes

```python
import asyncio

from ssllabs import Ssllabs

async def status_codes():
    ssllabs = Ssllabs()
    return await ssllabs.status_codes()

asyncio.run(status_codes())
```

This will give you a [StatusCodes object](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#statuscodes) as dataclass.

## Low level usage

If the high level methods do not match your use case, you can access each [API call](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#protocol-calls).

```python
import asyncio

from ssllabs.api import Endpoint

async def get_grade():
    api = Endpoint()
    endpoint = await api.get(host="devolo.de", s="195.201.179.93")
    return endpoint.grade
```

Classes are called like the [API call](https://github.com/ssllabs/ssllabs-scan/blob/master/ssllabs-api-docs-v3.md#protocol-calls) without the leading get. The get method will query the API. It will take the parameters like in the documentation and return a dataclass representing the object, the API describes. One exception in the naming: the getEndpointData call is implemented in the Endpoint class to be able to better distinguish it from its EndpointData result object.
