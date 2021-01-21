import httpx
import time
import asyncio

SSLLABS_URL = "https://api.ssllabs.com/api/v3/"

class Ssllabs:
    def __init__(self, url):
        self.url = url
        self.client = httpx.AsyncClient()
        
    def __del__(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.httpx.aclose())

    async def available(self):
        return (await self.client.get(f"{SSLLABS_URL}/info")).json()
    
    async def start_assessment(self, publish: bool = False, start_new: bool = True): 
        """[summary]

        Returns:
            [type]: [description]
        """
        data = {"host": self.host, "publish": publish, "start_new": start_new}
        return await self.client.get(f"{SSLLABS_URL}/analyze", params=data)
    
    async def get_assessment(self):
        start_time = time.time()
        while (await self.client.get(f"{SSLLABS_URL}/analyze", params={"host": self.url})).json()["status"] == "IN_PROGRESS": 
            if time.time() > start_time + 600:
                raise ValueError("CHANGE IT TO A TIMEOUT")
            print("waiting for result")
            time.sleep(5)
        return (await self.client.get(f"{SSLLABS_URL}/analyze", params={"host": self.url})).json()