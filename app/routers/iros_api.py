from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import iros_api_schemas, rest_response_schemas
from app.utils import iros_api_utils

router = APIRouter(
    prefix='/iros',
    tags=["등기부등본 API"]
)

r = iros_api_utils.IrosApiUtils()


@router.get('/search-road', description="도로명주소로 등기 검색")
async def get_search_road(payload: iros_api_schemas.GetRoad = Depends()):
    data = await r.get_road(payload)
    return {
        "data": data
    }


@router.get('/iros-info', description="등기발급 요청")
async def get_iros_info(iros_no: str):
    data = await r.get_iros(req_seq=0, iros_no=iros_no.replace("-", ""))
    return {
        "data": data
    }


@router.get('iros-info-detail', description="등기(갑을)상세")
async def get_iros_info_detail(or_seq: int):
    data = await r.get_iros_detail(mgr_seq=or_seq)
    return {
        "data": data
    }
