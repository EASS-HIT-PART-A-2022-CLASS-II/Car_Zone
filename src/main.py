import uvicorn
from fastapi import FastAPI
from urllib import request
from .models import *
import requests
import pytest

app = FastAPI()


@app.get("/gatallcars")
def gatallcars():
    res=requests.get("http://data.gov.il/api/3/action/datastore_search?resource_id=053cea08-09bc-40ec-8f7a-156f0677aff3")
    json_obj=res.json()
    return json_obj['result']['records']

@app.get("/tst/{car_id}")
def tst(car_id:int):
    res=requests.get("http://data.gov.il/api/3/action/datastore_search?resource_id=053cea08-09bc-40ec-8f7a-156f0677aff3")
    json_obj=res.json()
    for i in json_obj['result']['records']:
        if i['_id']==car_id:
            return i
    return json_obj 

@app.post("/tstpost",response_model=carRes,response_model_exclude_unset=True)
def getprice(car:carPost):
    res=requests.get("http://data.gov.il/api/3/action/datastore_search?resource_id=053cea08-09bc-40ec-8f7a-156f0677aff3")
    json_obj=res.json()
    for i in json_obj['result']['records']:
        if i['tozeret_cd']==car.manifacture & i['degem_cd']==car.modle:
            carRes.id=i['_id']
            carRes.mispar_rechev=i['mispar_rechev']
            return carRes
    carRes.error_code="500"
    carRes.id=0000
    return carRes


@app.get("/getcarcolor/{car_num}",response_model=carRes,response_model_exclude_unset=True)
def getcarcolor(car_num:int):
    res=requests.get("http://data.gov.il/api/3/action/datastore_search?resource_id=053cea08-09bc-40ec-8f7a-156f0677aff3")
    json_obj=res.json()
    for i in json_obj['result']['records']:
        if i['mispar_rechev']==car_num:
           carRes.id=i['_id']
           carRes.tzeva_rechev=i['tzeva_rechev']
           carRes.error_code="ok"
           return carRes
    carRes.id=0000
    carRes.error_code="ok"
    return carRes
   


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
