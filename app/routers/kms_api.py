from fastapi import APIRouter, HTTPException, Query
from app.utils import make_address_utils as address_utils, kms_api_utils
from typing_extensions import Annotated
from pydantic import Required

router = APIRouter(
    tags=["KMS API"],
    prefix="/ekms"
)

kms_api = kms_api_utils.KmsApiUtils()


@router.get("/junse_rate", description="전세가율 검색")
async def get_junse_rate(
        admCd: str = Query(description="법정동코드",
                           regex="[^a-zA-Zㄱ-힣]",
                           max_length=10)
):
    sigungu_code = address_utils.sido_gugun_code(admCd)
    return await kms_api.get_junse_rate(sigungu_code["sigunguCd"])


@router.get("/agency-info", description="중개업소 조회")
async def get_agency_info(sfl: str = Query(description="검색타입(defatult: 기본검색, boss: 대표자명, regNo: 등록번호, agency_nm: 상호명검색"),
                          stx: str = Query(description="검색어")
                          ):
    return await kms_api.get_agency_info(search_type=sfl, search_word=stx)

