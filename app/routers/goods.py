from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import goods_schemas, open_api_schemas, rest_response_schemas
from app.utils import escrow_utils, make_address_utils, open_api_util

router = APIRouter(
    tags=["물건 상태 관련 API"],
    prefix="/goods"
)

open_api = open_api_util.OpenApiUtils()


@router.get("/status-check", description="물건 상태 확인", response_model=rest_response_schemas.RestResponse)
async def goods_status_check(payload: goods_schemas.GoodsStatusCheckModel = Depends()):
    # 리턴할 내용
    info_obj = []
    # zerofill
    bun = payload.lnbrMnnm.zfill(4)
    ji = payload.lnbrSlno.zfill(4)
    platGbCd = payload.mtYn
    # 시군구 코드 쪼개기
    sigungu_code = make_address_utils.sido_gugun_code(payload.admCd)
    sigunguCd = sigungu_code["sigunguCd"]
    bjdongCd = sigungu_code["bjdongCd"]
    # 집합건물 / 비집합건물 분기
    if payload.hoNm:
        # 집합건물
        dongNm = None
        if payload.dongNm is not None:
            dongNm = escrow_utils.del_korean(payload.dongNm)

        _params = open_api_schemas.GetBrExposePubuseAreaInfo(
            sigunguCd=sigunguCd,
            bjdongCd=bjdongCd,
            bun=bun,
            ji=ji,
            platGbCd=platGbCd,
            dongNm=dongNm,
            hoNm=payload.hoNm,
            numOfRows=999
        )
        r = await open_api.get_br_expos_pubuse_area_info(_params)
        if r["response"]["header"]["resultCode"] != "00":
            raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail="공공데이터포털과 통신이 원활하지 않습니다")

        if r["response"]["body"]["items"] is not None:
            for item in r["response"]["body"]["items"]["item"]:
                # dongNm 과 hoNm이 같은 것만
                if item["dongNm"] == dongNm and item["hoNm"] == payload.hoNm and item["exposPubuseGbCd"] == "1":
                    info_obj.append({
                        "dongNm": item["dongNm"],
                        "hoNm": item["hoNm"],
                        "etcPurps": item["etcPurps"],
                        "etcStrct": item["etcStrct"],
                        "exposPubuseGbCd": item["exposPubuseGbCd"],
                        "exposPubuseGbCdNm": item["exposPubuseGbCdNm"],
                        "mainAtchGbCd": item["mainAtchGbCd"],
                        "mainAtchGbCdNm": item["mainAtchGbCdNm"],
                        "mainPurpsCd": item["mainPurpsCd"],
                        "mainPurpsCdNm": item["mainPurpsCdNm"]
                    })

        return {
            "data": info_obj
        }
    else:
        # 아닐 경우
        _params = open_api_schemas.GetBrTitleInfo(
            sigunguCd=sigunguCd,
            bjdongCd=bjdongCd,
            bun=bun,
            ji=ji,
            platGbCd=platGbCd,
            numOfRows=999
        )
        r = await open_api.get_br_title_info(_params)
        if r["response"]["header"]["resultCode"] != "00":
            raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail="공공데이터포털과 통신이 원활하지 않습니다")

        if r["response"]["body"]["items"] is not None:
            for item in r["response"]["body"]["items"]["item"]:
                # dongNm 과 hoNm이 같은 것만
                if item["exposPubuseGbCd"] == "1":
                    info_obj.append({
                        "etcPurps": item["etcPurps"],
                        "etcStrct": item["etcStrct"],
                        "exposPubuseGbCd": item["exposPubuseGbCd"],
                        "exposPubuseGbCdNm": item["exposPubuseGbCdNm"],
                        "mainAtchGbCd": item["mainAtchGbCd"],
                        "mainAtchGbCdNm": item["mainAtchGbCdNm"],
                        "mainPurpsCd": item["mainPurpsCd"],
                        "mainPurpsCdNm": item["mainPurpsCdNm"]
                    })
        return {
            "data": info_obj
        }
