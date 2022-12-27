from pydantic import BaseModel
from typing import Optional ,List

class carReq(BaseModel):
    manifacture: Optional[str]
    modle: Optional[str]

class carRes(BaseModel):
    id : int
    mispar_rechev : Optional[int]
    sug_degem : Optional[str]
    degem_nm : Optional[str]
    tozeret_nm : Optional[str]
    tzeva_rechev : Optional[str]
    moed_aliya_lakvish : Optional[str] 
    error_code : Optional[int]
    error_massage : Optional[str]
    class Config:
        orm_mode = True

class listOfCarRes(BaseModel):
    id : int
    car : List[carRes]
    error_code : int
    error_massage : str


''' TBD
class carRes(BaseModel):
    _id : int
    mispar_rechev : Optional[int]
    sug_degem : Optional[str]
    degem_cd : Optional[str]
    degem_nm : Optional[str]
    tozeret_cd : Optional[str]
    tozeret_nm : Optional[str]
    tzeva_cd : Optional[str]
    tzeva_rechev : Optional[str]
    moed_aliya_lakvish : Optional[str]
    ramat_gimur : Optional[str]
    ramat_eivzur_betihuty : Optional[str]
    kvutzat_zihum : Optional[str]
    shnat_yitzur : Optional[str]
    degem_manoa :Optional[str]
    mivchan_acharon_dt : Optional[str]
    tokef_dt :Optional[str]
    baalut : Optional[str]
    misgeret : Optional[str]
    zmig_kidmi :Optional[str]
    zmig_ahori :Optional[str]
    sug_delek_nm :Optional[str]
    horaat_rishum :Optional[str]
    kinuy_mishari :Optional[str]
    error_code : Optional[int]
    error_massage : Optional[str]
    def __init__(self,_id,mispar_rechev,sug_degem,degem_cd,degem_nm,tozeret_nm,tozeret_cd,tzeva_rechev,tzeva_cd,moed_aliya_lakvish,ramat_gimur,ramat_eivzur_betihuty,kvutzat_zihum,shnat_yitzur,degem_manoa,mivchan_acharon_dt,tokef_dt,baalut,misgeret,zmig_kidmi,zmig_ahori,sug_delek_nm,horaat_rishum,kinuy_mishari):
        self._id = _id
        self.mispar_rechev = mispar_rechev
        self.degem_nm = degem_nm
        self.degem_cd = degem_cd
        self.sug_degem = sug_degem
        self.tozeret_nm = tozeret_nm
        self.tozeret_cd = tozeret_cd
        self.tzeva_rechev = tzeva_rechev
        self.tzeva_cd =tzeva_cd
        self.moed_aliya_lakvish = moed_aliya_lakvish
        self.ramat_gimur = ramat_gimur
        self.ramat_eivzur_betihuty = ramat_eivzur_betihuty
        self.kvutzat_zihum = kvutzat_zihum
        self.shnat_yitzur = shnat_yitzur
        self.degem_manoa = degem_manoa
        self.mivchan_acharon_dt = mivchan_acharon_dt
        self.tokef_dt = tokef_dt
        self.baalut = baalut
        self.misgeret = misgeret
        self.zmig_kidmi = zmig_kidmi
        self.zmig_ahori = zmig_ahori
        self.sug_delek_nm = sug_delek_nm
        self.horaat_rishum = horaat_rishum
        self.kinuy_mishari = kinuy_mishari
    class Config:
        orm_mode = True
'''






