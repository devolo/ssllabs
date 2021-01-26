import asyncio
import logging
from abc import ABC

import httpx

API_VERSION = 3
SSLLABS_URL = f"https://api.ssllabs.com/api/v{API_VERSION}/"


class _Api(ABC):
    """Abstract class to communicate with Qualys SSL Labs Assessment APIs."""

    def __init__(self):
        self.logger = logging.getLogger(f"{self.__class__.__module__}.{self.__class__.__name__}")
        self.client = httpx.AsyncClient()

    def __del__(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.client.aclose())

    async def _call(self, api_endpoint: str, **kwargs) -> httpx.Response:
        """Invocate API."""
        r = await self.client.get(f"{SSLLABS_URL}{api_endpoint}", params=kwargs)
        r.raise_for_status()
        return r
