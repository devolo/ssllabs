import httpx
import time
import asyncio
import logging

SSLLABS_URL = "https://api.ssllabs.com/api/v3/"

class SsllabsApi:
    """[summary]
    """
    def __init__(self, url):
        """[summary]

        Args:
            url ([type]): [description]
        """
        self.url = url
        self.logger = logging.getLogger()
        self.client = httpx.AsyncClient()
        
    def __del__(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.client.aclose())

    async def available(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return await self.client.get(f"{SSLLABS_URL}/info")
    
    async def start_assessment(self, publish: bool = False, start_new: bool = True): 
        """[summary]

        Returns:
            [type]: [description]
        """
        data = {"host": self.url, "publish": publish, "start_new": start_new}
        return await self.client.get(f"{SSLLABS_URL}/analyze", params=data)
    
    async def get_assessment(self):
        """[summary]

        Raises:
            ValueError: [description]

        Returns:
            [type]: [description]
        """
        start_time = time.time()
        while (await self.client.get(f"{SSLLABS_URL}/analyze", params={"host": self.url})).json()["status"] == "IN_PROGRESS": 
            if time.time() > start_time + 600:
                raise ValueError("CHANGE IT TO A TIMEOUT")
            print("waiting for result")
            asyncio.sleep(10)
        return await self.client.get(f"{SSLLABS_URL}/analyze", params={"host": self.url})
    
    async def get_endpoint_data(self, endpoint: str):
        data = {"host": self.url, "s": endpoint}
        return await self.client.get(f"{SSLLABS_URL}/getEndpointData", params=data)