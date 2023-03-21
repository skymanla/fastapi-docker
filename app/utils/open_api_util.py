import requests, xmltodict, json


class OpenApiUtils:
    def __init__(self):
        self.service_key="%2FPFdCuaNh0SaZV5EN6MCQDdlH5mib745274FPIdt%2FZi46uxDlcZfqLyZ09cGbezHk7mv3YB8UOdaGgKrlEwWDA%3D%3D"
        self.decode_service_key="/PFdCuaNh0SaZV5EN6MCQDdlH5mib745274FPIdt/Zi46uxDlcZfqLyZ09cGbezHk7mv3YB8UOdaGgKrlEwWDA=="

    async def get_api(self, _url, _params, response_type="json"):
        if _params.get("serviceKey") is None:
            _params["serviceKey"] = self.decode_service_key
        r = requests.get(_url, params=_params)

        if response_type == "json":
            return r.json()
        elif response_type == "xml":
            _xml = r.content
            _xmltodict = xmltodict.parse(_xml)
            dic = json.loads(json.dumps(_xmltodict))
            return dic
        else:
            return r
