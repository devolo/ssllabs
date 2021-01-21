from .ssllabs_api import SsllabsApi
from .ssllabs_endpoint_data import EndpointData

class SsllabsReport(SsllabsApi):
    def __init__(self, url):
        super(SsllabsReport, self).__init__(url)
        
    def __del__(self):
        super().__del__()
    
    async def ssllabs_available(self):
        try:
            await self.available()
            return True
        except Exception:  # Find exceptions which can happen
            return False
    
    async def get_grades(self):
        report = await self.get_report()
        return {endpoint["ipAddress"]: endpoint["grade"] for endpoint in report["endpoints"]}
        
    async def get_report(self):
        return (await self.get_assessment()).json()
    
    async def get_endpoint_json(self, endpoint):
        # return (await self.get_endpoint_data(endpoint)).json()
        json = (await self.get_endpoint_data(endpoint)).json()
        ed = EndpointData(**json)
        print()
    
    async def get_worst_grade(self):
        grades = await self.get_grades()
        return chr(max([ord(value) for value in grades.values()]))