import uvicorn
from fastapi import FastAPI
import http.client
import pip._vendor.requests
import json

app = FastAPI()


@app.get("/")
def index():
    conn=http.client.HTTPSConnection("data.gov.il")
    conn.request("GET","/api/3/action/datastore_search?resource_id=053cea08-09bc-40ec-8f7a-156f0677aff3&limit=5")
    res=conn.getresponse()
    return {res.read()}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
