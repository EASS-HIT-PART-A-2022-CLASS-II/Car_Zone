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
  return response.json()

def main():
  sts.title("Car Zone")

  all_cars_button = sts.button("Get All Cars")
  manufacturer_button = sts.button("Get Cars by Manufacturer")
  #color_button = sts.button("Get Car Color")

  if all_cars_button:
      all = get_all_cars()
      jsonstr =json.dumps(all)
      data = json.loads(jsonstr)
      df = pd.DataFrame(data)
      st.dataframe(df)

  elif manufacturer_button:
    if "manifacture" not in st.session_state:
        st.session_state.manifacture = "0312"
        st.session_state.modle ="0014"
    st.button(
        "Get car",
        on_click=get_car_by,
        args=([st.session_state.manifacture + " " + st.session_state.modle]),
    ) 

  elif st.sidebar.button("Get data from backend"):
      if "car" not in st.session_state:
        st.session_state.car = "4284078"
      st.button(
        "Get color",
        on_click=get_color(st.session_state.car),
      )
    
def get_car_by(car):
  with st.form(key="test", clear_on_submit=True):
        col1, col2 = st.columns(2)
        manifacture = col1.text_input("Manifacture", car.split()[0], key="manifacture")
        modle = col2.text_input("Modle", car.split()[-1], key="modle")
        submit = st.form_submit_button(
            "Submit", on_click=show_car
        )

def show_car():
    car = get_cars_by_manufacturer(st.session_state.manifacture,st.session_state.modle)
    if car:
      st.json(car)


def get_color(car_num):
      with st.form(key="test", clear_on_submit=True):
        col1,col2 = st.columns(2)
        carcolor = col1.text_input("Enter car number", car_num, key="car")
        submit = st.form_submit_button(
            "Submit", on_click=show_color
        )
        

def show_color():
  st.write(st.session_state.car)
  entercar=int(st.session_state.car)+0
  st.write(type(entercar))
  res=get_car_color(entercar)
  st.json(res)


if __name__ == "__main__":
    main()

