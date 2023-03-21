from fastapi import APIRouter, Depends
from app.schemas import open_api_schemas
from app.utils import open_api_util

router = APIRouter(
    prefix="/open-api",
    tags=["공공데이터포털"]
)

r = open_api_util.OpenApiUtils()


@router.get("/land-frl-service", description="토지/지목,면적")
async def get_land_frl_service(payload: open_api_schemas.LandFrlService = Depends()):
    return await r.get_api(_url="http://apis.data.go.kr/1611000/nsdi/eios/LadfrlService/ladfrlList.xml",
                           _params=payload.dict(),
                           response_type="xml")


@router.get("/buld-ho-co-list", description="토지/대지권")
async def get_buld_ho_co_list(payload: open_api_schemas.BuldHoCoClist = Depends()):
    return await r.get_api(_url="http://apis.data.go.kr/1611000/nsdi/eios/LdaregService/buldHoCoList.xml",
                           _params=payload.dict(),
                           response_type="xml"
                           )


@router.get("/get-br-title-info", description="건물/구조용도,면적(비공동)")
async def get_br_title_info(payload: open_api_schemas.GetBrTitleInfo = Depends()):
    return await r.get_api(_url='http://apis.data.go.kr/1613000/BldRgstService_v2/getBrTitleInfo',
                           _params=payload.dict(),
                           response_type="json")


@router.get("/get-br-expos-pubuse-area-info", description="건물/구조용도,면적(공동)")
async def get_br_expos_pubuse_area_info(payload: open_api_schemas.GetBrExposePubuseAreaInfo = Depends()):
    return await r.get_api(_url='http://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposPubuseAreaInfo',
                           _params=payload.dict(),
                           response_type="json")
