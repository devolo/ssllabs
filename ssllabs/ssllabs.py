import asyncio

from .api.analyze import Analyze


class Ssllabs():
    async def analyze(self, host: str):
        api = Analyze()
        ready = False
        host_object = None
        while not ready:
            host_object = await api.get(host=host)
            ready = host_object.status == "READY"
            if ready:
                break
            await asyncio.sleep(10)
        return host_object
