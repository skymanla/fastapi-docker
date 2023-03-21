from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import kms_api_schemas, rest_response_schemas
from app.utils import kms_conn_utils

router = APIRouter(
    prefix='/kms',
    tags=["KMS API"]
)

r = kms_conn_utils.KmsConnUtils()


@router.get('/search-jibun', description="지번으로 등기 검색")
async def get_search_jibun(payload: kms_api_schemas.GetJibun = Depends()):
    data = await r.get_jibun(payload)
    return {
        "data": data.json()
    }


@router.get('/search-juso-apt-code', description="주소 & 단지코드 등기 검색")
async def get_search_juso_apt_code(payload: kms_api_schemas.GetJusoAndAptCode = Depends()):
    data = await r.get_juso_apt_code(payload)
    return {
        "data": data.json()
    }


@router.get('/search-law-code', description="법정동코드로 등기 검색")
async def get_search_law_code(payload: kms_api_schemas.GetLawCode = Depends()):
    data = await r.get_law_code(payload)
    return {
        "data": data.json()
    }


@router.get('/search-juso', description="주소로 등기 검색")
async def get_search_juso(payload: kms_api_schemas.GetJuso = Depends()):
    data = await r.get_juso(payload)
    return {
        "data": data.json()
    }


@router.get('/search-road', description="도로명주소로 등기 검색")
async def get_search_road(payload: kms_api_schemas.GetRoad = Depends()):
    data = await r.get_road(payload)
    return {
        "data": data.json()
    }


@router.get('/iros-info', description="등기발급 요청")
async def get_iros_info(req_seq: int, iros_no: str):
    data = await r.get_iros(req_seq, iros_no)
    return {
        "data": data.json()
    }


@router.get('/test-response', response_model=rest_response_schemas.RestResponse)
async def get_test_response():
    ab = 1
    if ab != 2:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="bad request")
    return {
        "code": "OK",
        "data": [
            {
                "test": 1111,
            },
            {
                "test": 2222,
            }
        ]
    }
