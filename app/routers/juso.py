from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import rest_response_schemas, juso_api_schemas
from app.utils import juso_api_utils

router = APIRouter(
    tags=["주소 검색 및 상세 정보"],
    prefix="/juso"
)

juso_utils = juso_api_utils.JusoApiUtils()


@router.get("/search", description="주소검색, return 값 중에서 admCd(법정동코드), rnMgtSn(도로주소코드)는 계속 가지고 가야함", response_model=rest_response_schemas.RestResponse)
async def search_juso(payload: juso_api_schemas.SearchAddress = Depends()):
    r = await juso_utils.get_address_detail(payload.keyword)
    if r["results"]["common"]["errorCode"] != "0":
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=r["results"]["common"]["errorMessage"])
    return {
        "data": r["results"]["juso"]
    }


@router.get("/search-dong-list", description="동 리스트, dongNm은 항상 가지고 가야함", response_model=rest_response_schemas.RestResponse)
async def search_dong_list(payload: juso_api_schemas.SearchDongList = Depends()):
    r = await juso_utils.get_dong_list(payload)
    if r["results"]["common"]["errorCode"] != "0":
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=r["results"]["common"]["errorMessage"])
    return {
        "data": r["results"]["juso"]
    }


@router.get("/search-ho-list", description="호 리스트, hoNm은 항상 가지고 가야함", response_model=rest_response_schemas.RestResponse)
async def search_ho_list(payload: juso_api_schemas.SearchHoList = Depends()):
    r = await juso_utils.get_ho_list(payload)
    if r["results"]["common"]["errorCode"] != "0":
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=r["results"]["common"]["errorMessage"])
    return {
        "data": r["results"]["juso"]
    }
