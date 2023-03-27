from pydantic import BaseModel, Field, validator
from typing import Union
from fastapi import Query
import re


class GoodsStatusCheckModel(BaseModel):
    admCd: str = Field(Query(description="법정동코드", max_length=10))
    mtYn: str = Field(Query(description="0 대지, 1 산, 2 블럭", regex=r'[0-2]{1}$'))
    lnbrMnnm: str = Field(Query(description="주소 본번"))
    lnbrSlno: str = Field(Query(description="주소 부번"))
    dongNm: Union[str, None] = Field(Query(description="동명", default=None))
    hoNm: Union[str, None] = Field(Query(description="호명", default=None))

    @validator('admCd')
    def validate_admCd(cls, value):
        if not re.match(r'^\d{10}$', value):
            raise ValueError('법정동코드 10자리를 입력해주세요')
        return value
