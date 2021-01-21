import httpx
import time

SSLLABS_URL = "https://api.ssllabs.com/api/v3/"

class Ssllabs:
    def __init__(self, url):
        self.url = url
        
    async def available(self):
        async with httpx.AsyncClient() as c:
            return (await c.get(f"{SSLLABS_URL}/info")).json()
    
    async def start_assessment(self, publish: bool = False, start_new: bool = True): 
        """[summary]

        Returns:
            [type]: [description]
        """
        data = {"host": self.host, "publish": publish, "start_new": start_new}
        async with httpx.AsyncClient() as c:
            return await c.get(f"{SSLLABS_URL}/analyze", params=data)
    
    async def get_assessment(self):
        start_time = time.time()
        async with httpx.AsyncClient() as c:
            while (await c.get(f"{SSLLABS_URL}/analyze", params={"host": self.url})).json()["status"] == "IN_PROGRESS": 
                if time.time() > start_time + 600:
                    raise ValueError("CHANGE IT TO A TIMEOUT")
                print("waiting for result")
                time.sleep(5)
            return (await c.get(f"{SSLLABS_URL}/analyze", params={"host": self.url})).json()