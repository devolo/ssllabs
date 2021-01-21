from .base_api import BaseApi
from ..data_classes.host_data_class import HostDataClass
from ..data_classes.endpoint_data_class import EndpointDataClass

class Analyze(BaseApi):
    def __init__(self):
        super(Analyze, self).__init__()
        
    def __del__(self):
        super().__del__()
        
    async def analyze(self, host) -> HostDataClass:
        r = await self._call(api_endpoint="analyze", host=host)
        json = r.json()
        json["endpoints"] = [EndpointDataClass(**x) for x in r.json()["endpoints"]]
        return HostDataClass(**json)
