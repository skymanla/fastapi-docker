import requests, xmltodict, json
from app.schemas import open_api_schemas

class OpenApiUtils:
    def __init__(self):
        self.url = "http://apis.data.go.kr"
        self.service_key="%2FPFdCuaNh0SaZV5EN6MCQDdlH5mib745274FPIdt%2FZi46uxDlcZfqLyZ09cGbezHk7mv3YB8UOdaGgKrlEwWDA%3D%3D"
        self.decode_service_key="/PFdCuaNh0SaZV5EN6MCQDdlH5mib745274FPIdt/Zi46uxDlcZfqLyZ09cGbezHk7mv3YB8UOdaGgKrlEwWDA=="

    async def get_api(self, durl, _params, response_type="json"):
        if _params.get("serviceKey") is None:
            _params["serviceKey"] = self.decode_service_key
        r = requests.get(self.url + durl, params=_params)
        print(r.url)
        if response_type == "json":
            return r.json()
        elif response_type == "xml":
            _xml = r.content
            _xmltodict = xmltodict.parse(_xml)
            dic = json.loads(json.dumps(_xmltodict))
            return dic
        else:
            return r

    async def get_br_title_info(self, _params: open_api_schemas.GetBrTitleInfo):
        return await self.get_api(
            durl="/1613000/BldRgstService_v2/getBrTitleInfo",
            _params=_params.dict(),
            response_type="xml"
        )

    async def get_br_expos_pubuse_area_info(self, _params: open_api_schemas.GetBrExposePubuseAreaInfo):
        return await self.get_api(
            durl="/1613000/BldRgstService_v2/getBrExposPubuseAreaInfo",
            _params=_params.dict(),
            response_type="xml"
        )
