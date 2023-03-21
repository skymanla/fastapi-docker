from pydantic import BaseModel, Field
from fastapi import Query


class SearchAddress(BaseModel):
    keyword: str = Field(Query(description="주소 검색어"))


class SearchDongList(BaseModel):
    admCd: str = Field(Query(description="admCd(법정동코드)", regex="[0-9]{10}"))
    rnMgtSn: str = Field(Query(description="rnMgtSn(도로명주소코드)", regex="[0-9]"))
    buldMnnm: int = Field(Query(description="buldMnnm(건물주번)"))
    buldSlno: int = Field(Query(description="buldSlno(건물부번)"))


class SearchHoList(BaseModel):
    admCd: str = Field(Query(description="admCd", regex="[0-9]{10}"))
    rnMgtSn: str = Field(Query(description="rnMgtSn", regex="[0-9]"))
    buldMnnm: int = Field(Query(description="buldMnnm"))
    buldSlno: int = Field(Query(description="buldSlno"))
    dongNm: str = Field(Query(description="dongNm(동이름)"))
