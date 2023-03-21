import requests
from app.schemas import kms_api_schemas


class KmsConnUtils:
    def __init__(self):
        self.conn = "http://in2.rsun.kr:53309/kms_tro_mgr"

    async def get_jibun(self, params: kms_api_schemas.GetJibun):
        _url = self.conn + "/sts/search/jibun/ReqPropNoByGdCodeAndRgdCode"
        print("params ======> ", params)
        r = requests.get(_url, params={
            "req-seq": params.reqSeq,
            "lawd-code": params.lawdCode,
            "apt-code": params.aptCode,
            "dong-code": params.dongCode,
            "jb-type": params.jbType,
            "jibun1": params.jibun1,
            "jibun2": params.jibun2,
            "dong-nm": params.dongNm,
            "flr-nm": params.flrNm,
            "room-nm": params.roomNm
        })
        return r

    async def get_juso_apt_code(self, params: kms_api_schemas.GetJusoAndAptCode):
        _url = self.conn + "/sts/search/jibun/ReqPropNoByGdCodeAndAddr"
        r = requests.get(_url, params={
            "req-seq": params.reqSeq,
            "sido": params.sido,
            "gugun": params.gugun,
            "ymd": params.ymd,
            "apt-code": params.aptCode,
            "dong-code": params.dongCode,
            "jb-type": params.jbType,
            "jibun1": params.jibun1,
            "jibun2": params.jibun2,
            "dong-nm": params.dongNm,
            "flr-nm": params.flrNm,
            "room-nm": params.roomNm
        })
        return r

    async def get_law_code(self, params: kms_api_schemas.GetLawCode):
        _url = self.conn + "/sts/search/jibun/ReqPropNoByRgdCode"
        r = requests.get(_url, params={
            "req-seq": params.reqSeq,
            "lawd-code": params.lawdCode,
            "jb-type": params.jbType,
            "jibun1": params.jibun1,
            "jibun2": params.jibun2,
            "dong-nm": params.dongNm,
            "flr-nm": params.flrNm,
            "room-nm": params.roomNm
        })
        return r

    async def get_juso(self, params: kms_api_schemas.GetJuso):
        _url = self.conn + "/sts/search/jibun/ReqPropNoByAddr"
        r = requests.get(_url, params={
            "req-seq": params.reqSeq,
            "sido": params.sido,
            "gugun": params.gugun,
            "ymd": params.ymd,
            "jb-type": params.jbType,
            "jibun1": params.jibun1,
            "jibun2": params.jibun2,
            "dong-nm": params.dongNm,
            "flr-nm": params.flrNm,
            "room-nm": params.roomNm
        })
        return r

    async def get_road(self, params: kms_api_schemas.GetRoad):
        _url = self.conn + "/sts/search/road/ReqByRdNmAndBdNo"
        r = requests.get(_url, params={
            "req-seq": params.reqSeq,
            "sido": params.sido,
            "gugun": params.gugun,
            "road-nm": params.roadNm,
            "bd-no": params.bdNo,
            "dong-nm": params.dongNm,
            "room-nm": params.roomNm
        })
        return r

    async def get_iros(self, req_seq: int, iros_no: str):
        _url = self.conn + "/sts/issue/ReqIssByRegisNo"
        r = requests.get(_url, params={
            "req-seq": req_seq,
            "iros-no": iros_no
        })
        return r
