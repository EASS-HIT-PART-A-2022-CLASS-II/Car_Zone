import requests
import streamlit as st
from streamlit import sidebar as sts
import json
import pandas as pd

def get_all_cars():
  response =requests.get(f"http://backend:8000/gatallcars")
  return response.json()

def get_cars_by_manufacturer(manifacture: str, modle: str):
    data = {"manifacture": manifacture, "modle": modle}
    response = requests.post("http://backend:8000/getcarsbymanyfacture", json=data)
    return response.json()

def get_car_color(car_num:str):
  response = requests.get(f"http://backend:8000/getcarcolor/{car_num}")
  return response.json()



def main():
    
  all_cars_button = sts.button("Get All Cars")
  manufacturer_button = sts.button("Get Cars by Manufacturer and modle")
  color_button = sts.button("Get Car Color by car number")

  if all_cars_button:
      all = get_all_cars()
      jsonstr =json.dumps(all)
      data = json.loads(jsonstr)
      df = pd.DataFrame(data)
      st.dataframe(df)

  elif manufacturer_button:
    if "manifacture" not in st.session_state:
      st.session_state.manifacture = "0253"
      st.session_state.modle ="0028"
    st.button(
        "Get car",
        on_click=get_car_by,
        args=([st.session_state.manifacture + " " + st.session_state.modle])
    ) 

  elif color_button:
    if "car" not in st.session_state:
        st.session_state.car = "1000132"
    st.button(
        "Get car color",
        on_click=get_color,
        args=([st.session_state.car])
      )

    
def get_car_by(car):
  with st.form(key="manifacture", clear_on_submit=True):
        col1, col2 = st.columns(2)
        manifacture = col1.text_input("Manifacture", car.split()[0], key="manifacture")
        modle = col2.text_input("Modle", car.split()[-1], key="modle")
        submit = st.form_submit_button(
            "Get car", on_click=show_car
        )

def show_car():
    car = get_cars_by_manufacturer(st.session_state.manifacture,st.session_state.modle)
    #if car['car'][0]['error_code']:
    jsonstr =json.dumps(car['car'])
    data = json.loads(jsonstr)
    df = pd.DataFrame(data)
    st.dataframe(df)
      #st.json(car)


def get_color(car_num):
      with st.form(key="car",clear_on_submit=True):
        col1 = st.columns(1)
        carcolor = col1[0].text_input("Enter car number", car_num, key="car")
        submit = st.form_submit_button(
            "Get color", on_click=show_color
        )
        
def show_color():
  res=get_car_color(st.session_state.car)
  if res['error_code']==200:
    st.write(f"The color of the car is : {res['tzeva_rechev']}")
  else:
    st.write("car not found")



with st.container():
  st.markdown(
    """
    <style>
        body {
            background-color: #fffff;
        }
    </style>
    """
    , unsafe_allow_html=True)
  main()
