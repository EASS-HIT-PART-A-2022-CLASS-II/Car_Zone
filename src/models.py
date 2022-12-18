from pydantic import BaseModel
from typing import Optional

class carPost(BaseModel):
    manifacture: Optional[str]
    modle: Optional[str]

class carRes(BaseModel):
    id : int
    mispar_rechev : Optional[int]
    sug_degem : Optional[str]
    degem_cd : Optional[str]
    degem_nm : Optional[str]
    tozeret_cd : Optional[str]
    tozeret_nm : Optional[str]
    tzeva_cd : Optional[str]
    tzeva_rechev : Optional[str]
    moed_aliya_lakvish : Optional[str]
    error_code : Optional[str]
    class Config:
        orm_mode = True

    



