from pydantic import BaseModel, Field
from typing import Union
from fastapi import Query


class StepOneSchemas(BaseModel):
    roadAddress: str = Field(Query(description="도로명주소"))
    jibunAddress: str = Field(Query(description="지번주소"))
    bcode: str = Field(Query(description="법정동코드(10자리)", max_length=10, regex='[0-9]{10}'))
    sido: str = Field(Query(description="시도"))
    sigungu: str = Field(Query(description="시군구"))
    bname: str = Field(Query(description="읍면동"))
    zoneCode: Union[str, None] = Field(Query(description="우편번호", default=None))
    sigunguCode: str = Field(Query(description="시군구법정코드(5자리)", regex='[0-9]{5}'))
    roadname: str = Field(Query(description="도로명"))
    apartment: str = Field(Query(description="공동주택여부(Y/N)", max_length=1))
    dongNm: Union[str, None] = Field(Query(description="동명(숫자만 기입)", default=None))
    hoNm: Union[str, None] = Field(Query(description="호명(숫자만 기입)", default=None))


class GetDongHoSchemas(BaseModel):
    bcode: str = Field(Query(description="법정동코드", max_length=10, regex='[0-9]{10}'))
    jibunAddress: str = Field(Query(description="지번주소"))
    dong: str = Field(Query(description="동", regex='[0-9]'))
    ho: str = Field(Query(description="호(데이터는 int형으로 내려가지만 줄 때는 str 형태로", regex='[0-9]'))


