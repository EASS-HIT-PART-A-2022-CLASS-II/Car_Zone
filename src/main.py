import uvicorn
from fastapi import FastAPI
from src.models import *
import requests

app = FastAPI()

''' TBD
@app.get("/gatallcars",response_model=listOfCarRes,response_model_exclude_unset=True)
def gatallcars():
    res=requests.get("http://data.gov.il/api/3/action/datastore_search?resource_id=053cea08-09bc-40ec-8f7a-156f0677aff3")
    json_obj=res.json()
    listOfCars : List[carRes] = [carRes(**car) for car in json_obj['result']['records']]
    return listOfCars #json_obj['result']['records']
'''
@app.get("/gatallcars")
def gatallcars():
    res=requests.get("http://data.gov.il/api/3/action/datastore_search?resource_id=053cea08-09bc-40ec-8f7a-156f0677aff3")
    json_obj=res.json()
    return json_obj['result']['records']

''' TBD
@app.post("/getcarsby",response_model=listOfCarRes,response_model_exclude_unset=True)
def getprice(car:carReq):
    res=requests.get("http://data.gov.il/api/3/action/datastore_search?resource_id=053cea08-09bc-40ec-8f7a-156f0677aff3")
    json_obj=res.json()
    listOfCars : List[carRes] = [carRes(**car) for car in json_obj]
    return listOfCars
'''

@app.post("/getcarsbymanyfacture",response_model=listOfCarRes,response_model_exclude_unset=True)
def getlist(car:carReq)->listOfCarRes:
    res=requests.get("http://data.gov.il/api/3/action/datastore_search?resource_id=053cea08-09bc-40ec-8f7a-156f0677aff3")
    json_obj = res.json()
    cars = listOfCarRes(
        id=1,
        error_code=200,
        error_massage="OK",
        car=[]
    )
    for i in json_obj['result']['records']:
        if (i['tozeret_cd'] == car.manifacture) & (i['degem_cd'] == car.modle):
            carinput = carRes(
                id=i['_id'],
                mispar_rechev=i['mispar_rechev'],
                sug_degem=i['sug_degem'],
                degem_nm=i['degem_nm'],
                tozeret_nm=i['tozeret_nm'],
                tzeva_rechev=i['tzeva_rechev'],
                moed_aliya_lakvish=i['moed_aliya_lakvish'],
                error_code=200,
                error_massage="OK"
            )
            cars.car.append(carinput)
    if not cars.car:
        cars = listOfCarRes(
            id=000,
            error_code=500,
            error_massage="OK",
            car=[]
        )    
    return cars


@app.get("/getcarcolor/{car_num}",response_model=carRes,response_model_exclude_unset=True)
def getcarcolor(car_num:str):
    res=requests.get("http://data.gov.il/api/3/action/datastore_search?resource_id=053cea08-09bc-40ec-8f7a-156f0677aff3")
    json_obj=res.json()
    carRes.tzeva_rechev=""
    for i in json_obj['result']['records']:
        if i['mispar_rechev']==int(car_num):
           carRes.id=i['_id']
           carRes.tzeva_rechev=i['tzeva_rechev']
           carRes.error_code=200
           carRes.error_massage="OK"
           return carRes
    carRes.id=0000
    carRes.error_code=500
    carRes.error_massage="car not found"
    return carRes

if __name__ == "__main__":
    uvicorn.run("main:app",host='0.0.0.0', port=8000, reload=True)

