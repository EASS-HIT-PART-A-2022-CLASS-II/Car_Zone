from .main import *
from fastapi.testclient import TestClient
 #import requests

client = TestClient(app)

ENDPOINT ="http://127.0.0.1:8000/docs#/default"

def test_getcarcolor():     #test sucsses
    response=getcarcolor("1000132")
    assert response.error_code==200 

def test_getcarcolor1():    
    response=getcarcolor("111")
    assert response.error_massage=="car not found"

def test_getlist():      #test sucsses
    payload={
            "manifacture": "0481",
            "modle": "0652"
            }
    response= client.post("/getcarsbymanyfacture", json=payload)
    assert response.status_code==200

