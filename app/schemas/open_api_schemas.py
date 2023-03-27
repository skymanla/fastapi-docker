from pydantic import BaseModel, Field
from typing import Union, List
from fastapi import Query


class LandFrlService(BaseModel):
    pnu: str = Field(description="필지(고유번호)", max_length=19)


class BuldHoCoClist(BaseModel):
    pnu: str = Field(description="필지(고유번호)", max_length=19)
    agbldgSn: Union[str, None] = Field(description="대지권일련번호", default=None, max_length=4)
    buldDongNm: Union[str, None] = Field(description="동명", default=None)
    buldFloorNm: Union[str, None] = Field(description="층명", default=None)
    buldHoNm: Union[str, None] = Field(description="호명", default=None)


class GetBrTitleInfo(BaseModel):
    sigunguCd: str = Field(description="시군구코드(5자리)", max_length=5)
    bjdongCd: str = Field(description="동코드(5자리)", max_length=5)
    platGbCd: str = Field(description="대지구분코드 0: 대지, 1: 산, 2:블록", max_length=1)
    bun: str = Field(description="본번(번)", max_length=4)
    ji: str = Field(description="부번(지)", max_length=4)
    startDate: Union[str, None] = Field(description="검색시작일(YYYYMMDD)", default=None, max_length=8)
    endDate: Union[str, None] = Field(description="검색종료일(YYYYMMDD)", default=None, max_length=8)
    numOfRows: Union[str, None] = Field(description="리스트수", default=None, max_length=3)
    pageNo: Union[str, None] = Field(description="페이지번호", default=None, max_length=3)
    _type: Union[str, None] = Field(description="리턴 형태(xml, json)", default="json")


class GetBrExposePubuseAreaInfo(BaseModel):
    sigunguCd: str = Field(description="시군구코드(5자리)", max_length=5)
    bjdongCd: str = Field(description="동코드(5자리)", max_length=5)
    platGbCd: str = Field(description="대지구분코드 0: 대지, 1: 산, 2:블록", max_length=1)
    bun: str = Field(description="본번", max_length=4)
    ji: str = Field(description="부번", max_length=4)
    dongNm: Union[str, None] = Field(description="동명칭(ex: n)", max_length=100, default=None)
    hoNm: str = Field(description="호명칭(ex: n호)", max_length=100)
    startDate: Union[str, None] = Field(description="검색시작일(YYYYMMDD)", default=None, max_length=8)
    endDate: Union[str, None] = Field(description="검색종료일(YYYYMMDD)", default=None, max_length=8)
    numOfRows: Union[str, None] = Field(description="리스트수", default=None, max_length=3)
    pageNo: Union[str, None] = Field(description="페이지번호", default=None, max_length=3)
    _type: Union[str, None] = Field(description="리턴 형태(xml, json)", default="json")

