from .base_api import BaseApi
from ..data_classes.endpoint_data_class import EndpointDataClass

class EndpointData(BaseApi):
    def __init__(self):
        super(EndpointData, self).__init__()
        
    def __del__(self):
        super().__del__()
        
    async def get_endpoint_data(self, host, endpoint_ip):
        r = await self._call(api_endpoint="getEndpointData", host=host, s=endpoint_ip)
        return EndpointDataClass(**r.json())