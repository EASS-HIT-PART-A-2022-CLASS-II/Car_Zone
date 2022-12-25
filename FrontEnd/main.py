import requests
import streamlit as st
from streamlit import sidebar as sts
import json
import pandas as pd

def get_all_cars():
  response =requests.get(f"http://localhost:8000/gatallcars")
  return response.json()

def get_cars_by_manufacturer(manifacture: str, modle: str):
    data = {"manifacture": manifacture, "modle": modle}
    response = requests.post("http://localhost:8000/getcarsbymanyfacture", json=data)
    return response.json()

def get_car_color(car_num):
  response = requests.get("http://localhost:8000/getcarcolor/{car_num}")
  data = response.json()
  return data

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
    
    color_data = sts.button("Enter car")
    if color_button:
      color=get_car_color(color_data)
      st.json(color)

    if st.sidebar.button("Get data from backend"):
      carinput = st.text_input("Entre car number")
      if carinput:
        car = get_car_color(int(carinput))

        # Check the status code of the response
        if car.status_code == 200:
          # If the status code is 200, get the data from the response
          data = car.json()

          # Display the data in the frontend
          st.write(data)
        else:
          # If the status code is not 200, display an error message
          st.write("Error: failed to get data from backend")
        #for item in data:
        #  for key, value in item.items():
        #    if key == "_id":
        #      key = "Id"
        #    if key == "mispar_rechev":
        #      key = "Car Number"
        #    st.write(key, value)



if __name__ == "__main__":
  main()
