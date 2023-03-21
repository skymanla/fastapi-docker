import requests
from app.schemas import juso_api_schemas


class JusoApiUtils:
    def __init__(self):
        self.confirm_key_normal = "U01TX0FVVEgyMDIzMDMyMDEzMzczMzExMzYwNjg="
        self.confirm_key_detail = "U01TX0FVVEgyMDIzMDMyMDEzMzg1NDExMzYwNjk="
        self._url = "https://business.juso.go.kr/addrlink/addrLinkApi.do"
        self._url_jsonp = "https://business.juso.go.kr/addrlink/addrLinkApiJsonp.do"
        self._url_detail = "https://business.juso.go.kr/addrlink/addrDetailApi.do"

    async def get_address_detail(self, keyword: str):
        _params = {
            "confmKey": self.confirm_key_normal,
            "currnetPage": 1,
            "countPerPage": 20,
            "keyword": keyword,
            "resultType": "json"
        }
        r = requests.get(self._url, params=_params)
        return r.json()

    async def get_dong_list(self, _params: juso_api_schemas.SearchDongList):
        params = {
            "confmKey": self.confirm_key_detail,
            "admCd": _params.admCd,
            "rnMgtSn": _params.rnMgtSn,
            "udrtYn": "0",
            "buldMnnm": _params.buldMnnm,
            "buldSlno": _params.buldSlno,
            "resultType": "json",
            "searchType": "dong"
        }

        r = requests.get(self._url_detail, params=params)
        return r.json()

    async def get_ho_list(self, _params: juso_api_schemas.SearchHoList):
        params = {
            "confmKey": self.confirm_key_detail,
            "admCd": _params.admCd,
            "rnMgtSn": _params.rnMgtSn,
            "udrtYn": "0",
            "buldMnnm": _params.buldMnnm,
            "buldSlno": _params.buldSlno,
            "resultType": "json",
            "searchType": "floorhr",
            "dongNm": _params.dongNm
        }

        r = requests.get(self._url_detail, params=params)
        return r.json()


