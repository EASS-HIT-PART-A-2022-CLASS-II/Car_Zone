import requests
import streamlit as st
from streamlit import sidebar as sts
import json
import pandas as pd
from ..src.models import *

def get_all_cars():
  response =requests.get(f"http://localhost:8000/gatallcars")
  return response.json()

def get_cars_by_manufacturer(manifacture: str, modle: str):
    data = {"manifacture": manifacture, "modle": modle}
    response = requests.post("http://localhost:8000/getcarsbymanyfacture", json=data)
    return response.json()

def get_car_color(car_num):
  # Send a GET request to your FastAPI endpoint
  response = requests.get(f"http://localhost:8000/getcarcolor/{car_num}")
  # Convert the response to a Python dictionary
  data = response.json()
  return data


#manufacturer_input = st.sidebar.selectbox("Select Manufacturer", manufacturer_options)
#model_input = st.sidebar.text_input("Enter Model")

#car_number_input = st.sidebar.text_input("Enter Car Number")
def main():
    sts.title("Car Zone")

    all_cars_button = sts.button("Get All Cars")
    manufacturer_button = sts.button("Get Cars by Manufacturer")
    color_button = sts.button("Get Car Color")

    if all_cars_button:
        all = get_all_cars()
        jsonstr =json.dumps(all)
        data = json.loads(jsonstr)
        df = pd.DataFrame(data)
        st.dataframe(df)
    if manufacturer_button:
      manifacture = st.sidebar.text_input("Manifacture")
      modle = st.sidebar.text_input("Modle")
      car = get_cars_by_manufacturer(manifacture,modle)

    if st.sidebar.button("tst"):
      car= st.text_input("Car number")
      if st.button("Get color"):
        data = get_car_color(car)
        if data is not None:
        # If the error code is 200, display the car color
          if data.error_code == 200:
            st.write(f"Color: {data.tzeva_rechev}")
          else:
            # If the error code is not 200, display an error message
            st.write("Error: car not found")
        else:
          st.write("Error: response is None")
        #for item in data:
        #  for key, value in item.items():
        #    if key == "_id":
        #      key = "Id"
        #    if key == "mispar_rechev":
        #      key = "Car Number"
        #    st.write(key, value)



if __name__ == "__main__":
  main()
