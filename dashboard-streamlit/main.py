from operator import ne
import streamlit as st
from data.get_data import anual_pop_gender, neighborhood

st.title("Population and Unemployment in Barcelona")
st.text("Mid-Project Bootcamp CoreCodeSchool")

nei = neighborhood

ls = st.multiselect("Neighborhood Select", nei)

[neighborhood(barrios) for barrios in ls]