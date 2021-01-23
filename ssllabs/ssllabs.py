import asyncio

from .api.analyze import Analyze


class Ssllabs():

    async def analyze(self, host: str):
        api = Analyze()
        host_object = await api.get(host=host)
        while host_object.status not in ["READY", "ERROR"]:
            await asyncio.sleep(10)
            host_object = await api.get(host=host)
        return host_object
