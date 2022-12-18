from pydantic import BaseModel
from typing import Optional

class carPost(BaseModel):
    manifacture:int
    modle:int

class carRes(BaseModel):
    id : int
    mispar_rechev : Optional[int]
    sug_degem : Optional[str]
    degem_cd : Optional[int]
    degem_nm : Optional[str]
    tozeret_cd : Optional[int]
    tozeret_nm : Optional[str]
    tzeva_cd : Optional[int]
    tzeva_rechev : Optional[str]
    moed_aliya_lakvish : Optional[str]
    



