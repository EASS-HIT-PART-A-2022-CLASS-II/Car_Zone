from .main import *
from fastapi.testclient import TestClient
 #import requests

client = TestClient(app)

ENDPOINT ="http://127.0.0.1:8000/docs#/default"

def test_getcarcolor():     #test sucsses
    response=getcarcolor("1000132")
    assert response.error_code==200 

def test_getcarcolor1():    #test failure
    response=getcarcolor("1000132")
    assert response.error_massage=="aaa" 

def test_getlist():      #test sucsses
    payload={
            "manifacture": "0299",
            "modle": "0055"
            }
    response= client.post("/getcarsbymanyfacture", json=payload)
    #response=requests.post(ENDPOINT + "/" +"getlist_getcarsbymanyfacture_post" , json=payload) 
    assert response.error_code==200

