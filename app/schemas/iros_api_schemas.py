from pydantic import BaseModel, Field
from typing import Union
from fastapi import Query


class GetJibun(BaseModel):
    reqSeq: Union[int, None] = Field(Query(description="요청자순번(KMS)", default=0))
    lawdCode: str = Field(Query(description="법정동코드"))
    aptCode: int = Field(Query(description="단지코드"))
    dongCode: int = Field(Query(description="동코드"))
    jbType: int = Field(Query(description="번지구분 0: 일반, 1: 산"))
    jibun1: str = Field(Query(description="본번"))
    jibun2: Union[str, None] = Field(Query(description="부번", default=None))
    dongNm: Union[str, None] = Field(Query(description="동명", default=None))
    flrNm: Union[str, None] = Field(Query(description="층명 -n: 지하, n: 지상", default=None))
    roomNm: str = Field(Query(description="호명"))


class GetJusoAndAptCode(BaseModel):
    reqSeq: Union[int, None] = Field(Query(description="요청자순번(KMS)", default=0))
    sido: str = Field(Query(description="시도"))
    gugun: str = Field(Query(description="구군"))
    ymd: str = Field(Query(description="읍면동"))
    aptCode: int = Field(Query(description="단지코드"))
    dongCode: int = Field(Query(description="동코드"))
    jbType: int = Field(Query(description="번지구분 0: 일반, 1: 산"))
    jibun1: str = Field(Query(description="본번"))
    jibun2: Union[str, None] = Field(Query(description="부번", default=None))
    dongNm: Union[str, None] = Field(Query(description="동명", default=None))
    flrNm: Union[str, None] = Field(Query(description="층명 -n: 지하, n: 지상", default=None))
    roomNm: str = Field(Query(description="호명"))


class GetLawCode(BaseModel):
    reqSeq: Union[int, None] = Field(Query(description="요청자순번(KMS)", default=0))
    lawdCode: str = Field(Query(description="법정동코드"))
    jbType: int = Field(Query(description="번지구분 0: 일반, 1: 산", max_size=1))
    jibun1: str = Field(Query(description="본번"))
    jibun2: Union[str, None] = Field(Query(description="부번", default=None))
    dongNm: Union[str, None] = Field(Query(description="동명", default=None))
    flrNm: Union[str, None] = Field(Query(description="층명 -n: 지하, n: 지상", default=None))
    roomNm: str = Field(Query(description="호명"))


class GetJuso(BaseModel):
    reqSeq: Union[int, None] = Field(Query(description="요청자순번(KMS)", default=0))
    sido: str = Field(Query(description="시도"))
    gugun: str = Field(Query(description="구군"))
    ymd: str = Field(Query(description="읍면동"))
    jbType: int = Field(Query(description="번지구분 0: 일반, 1: 산"))
    jibun1: str = Field(Query(description="본번"))
    jibun2: Union[str, None] = Field(Query(description="부번", default=None))
    dongNm: Union[str, None] = Field(Query(description="동명", default=None))
    flrNm: Union[str, None] = Field(Query(description="층명 -n: 지하, n: 지상", default=None))
    roomNm: str = Field(Query(description="호명"))


class GetRoad(BaseModel):
    siNm: str = Field(Query(description="시도"))
    sggNm: str = Field(Query(description="구군"))
    rn: str = Field(Query(description="도로명"))
    bdNo: str = Field(Query(description="건물번호 {buldMnnm}-{buldSlno} ex) buldSlno가 0이 아니면 {buldMnnm}-{buldSlno} 0이거나 없으면 {buldMnnm}"))
    dongNm: Union[str, None] = Field(Query(description="동명(동이 있을 경우, 없을 시 안 보내도 됨)", default=None))
    hoNm: str = Field(Query(description="호명"))


class ItemsObject:
    irosNo: str = Field(Query(description="등기번호"))
    owner: str = Field(Query(description="소유자"))
    addr: str = Field(Query(description="소재지번"))
    propType: str = Field(Query(description="집합건물 표시"))


class ResponseIros(BaseModel):
    resultCount: int = Field(Query(description="결과코드, 1: 성공, 2: 실패"))
    resultMsg: Union[str, None] = Field(Query(description="결과메세지", default=None))
    reqSeq: int = Field(Query(description="요청자 작업순번"))
    orSeq: int = Field(Query(description="통합등기소 순번"))
    totalCnt: Union[int, None] = Field(Query(description="아이템 개수", default=0))
    items: Union[object, None] = Field(Query(description="객체 리스트"))





