import requests


async def get_data(url: str, params: dict):
    r = requests.get(url, params=params)
    return r.json()


class KmsApiUtils:
    def __init__(self):
        self.serviceKey = "29bd31b10e7dafc754f0"
        self._url = "https://apis.rsun.kr/st"
        self._params = {
            "service-key": self.serviceKey,
        }

    # 시군구코드로 전세가율 가져오기
    async def get_junse_rate(self, sigungu_code: str):
        url = self._url + "/safety-trade-service/rentpricerate"
        self._params["sigungu-code"] = sigungu_code

        return await get_data(url, self._params)

    async def get_agency_info(self, search_type: str, search_word: str):
        if search_type == "default":
            url = self._url + "/safety-trade-service/agencyinfo"
        elif search_type == "boss":
            url = self._url + "/safety-trade-service/agencyinforep"
        elif search_type == "regNo":
            url = self._url + "/safety-trade-service/agencyinforegno"
        else:
            url = self._url + "/safety-trade-service/agencyinfoagencynm"
        self._params["search-word"] = search_word

        return await get_data(url, self._params)



