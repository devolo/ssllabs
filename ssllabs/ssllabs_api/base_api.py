import httpx
import time
import asyncio
import logging

SSLLABS_URL = "https://api.ssllabs.com/api/v3/"

class BaseApi:
    """[summary]
    """
    def __init__(self):
        """[summary]

        Args:
            url ([type]): [description]
        """
        self.logger = logging.getLogger()
        self.client = httpx.AsyncClient()
        
    def __del__(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.client.aclose())
        
    async def _call(self, api_endpoint, **kwargs):
        return await self.client.get(f"{SSLLABS_URL}{api_endpoint}", params=kwargs)