import asyncio

from .api.analyze import Analyze


class Ssllabs():

    async def analyze(self, host: str):
        api = Analyze()
        ready = False
        host_object = await api.get(host=host)
        while not ready:
            await asyncio.sleep(10)
            host_object = await api.get(host=host)
            ready = host_object.status == "READY"  # ToDo: Handle status ERROR
        return host_object
