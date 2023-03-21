from fastapi import APIRouter, HTTPException, Depends, status
from app.schemas import rest_response_schemas, step_one_schemas
from app.utils import open_api_util, make_address_utils

router = APIRouter(
    tags=["진입화면쪽"],
    prefix="/step-one"
)

open_api = open_api_util.OpenApiUtils()


@router.get("/has-possession-ledger", response_model=rest_response_schemas.RestResponse, description="전유부 존재")
async def has_possession_ledger(payload: step_one_schemas.StepOneSchemas = Depends()):
    _params = {}
    bun_ji_obj = make_address_utils.make_bun_ji(payload.jibunAddress)
    _params["sigunguCd"] = payload.sigunguCode
    _params["bjdongCd"] = payload.bcode.replace(_params["sigunguCd"], "")
    _params["platGbCd"] = "0"
    _params["bun"] = bun_ji_obj["bun"]
    _params["ji"] = bun_ji_obj["ji"]

    _url = "http://apis.data.go.kr/1613000/BldRgstService_v2/getBrTitleInfo"
    if payload.apartment == "Y":
        # 동호 정보 만들기 위해서
        _params["numOfRows"] = "999"
        _params["pageNo"] = "1"
        _url = "http://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposPubuseAreaInfo"

    try:
        r = await open_api.get_api(
            _url=_url,
            _params=_params,
            response_type="xml"
        )

        response_body = r["response"]["body"]
        possession_ledger = False
        dong_ho_list = []
        if isinstance(response_body["items"], dict):
            item = response_body["items"]["item"]
            if isinstance(item, list):
                for i in item:
                    if i["regstrKindCdNm"] == "전유부":
                        possession_ledger = True
                        break
                # make dong_ho_list
                dong_ho_list = make_address_utils.make_dong_ho(item)
            elif isinstance(item, dict):
                possession_ledger = True if item["regstrKindCdNm"] == "전유부" else False

        return {
            "data": {
                "possessionLedger": possession_ledger,
                "dongHoList": dong_ho_list
            }
        }
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ex.__class__.__name__)


@router.get("/get-area-info", description="동호받아서 전유부 상세 확인")
async def get_br_expose_area_info(payload: step_one_schemas.GetDongHoSchemas = Depends()):
    _url = "http://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposPubuseAreaInfo"
    _params = {}
    sido_gu_gun_code = make_address_utils.make_sido_gugun_code(payload.bcode)
    bun_ji_obj = make_address_utils.make_bun_ji(payload.jibunAddress)
    _params["sigunguCd"] = sido_gu_gun_code["sigunguCd"]
    _params["bjdongCd"] = sido_gu_gun_code["bjdongCd"]
    _params["platGbCd"] = "0"
    _params["bun"] = bun_ji_obj["bun"]
    _params["ji"] = bun_ji_obj["ji"]
    # 검색 갯수 최대한 땡겨서 하기 위함 page 건으로 쳤을 시 연산속도에 의해 빠른 커넥션이 발생해서 ip block 당할 우려가 있음
    _params["numOfRows"] = "9999"
    _params['dongNm'] = payload.dong
    _params['hoNm'] = payload.ho
    try:
        r = await open_api.get_api(
            _url=_url,
            _params=_params,
            response_type="xml"
        )

        r_body = r["response"]["body"]
        area_info = {
            "mainAtchNm": "주건축물",
            "mainAtchCd": 0
        }
        if isinstance(r_body["items"], dict):
            item = r_body["items"]["item"]
            if isinstance(item, list):
                for _i, _v in enumerate(item):
                    if _v["mainAtchGbCd"] >= 5000 or (_v["mainAtchGbCd"] < 5000 and _v["mainAtchGb"] >= 2003):
                        area_info.mainAtchNm = _v["mainAtchGbCdNm"]
                        area_info.mainAtchCd = _v["mainAtchGbCd"]
                        break

        return {
            "data": area_info
        }
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ex.__class__.__name__)

