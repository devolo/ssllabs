from .base_api import BaseApi
from ..data_classes.info_data_class import InfoData

class Info(BaseApi):
    def __init__(self, url):
        super(Info, self).__init__(url)
        
    def __del__(self):
        super().__del__()
    
    async def get_info(self) -> InfoData:
        r = await self._call("info")
        return InfoData(**r.json())
