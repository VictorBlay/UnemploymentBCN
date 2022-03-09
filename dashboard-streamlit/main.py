from operator import ne
import streamlit as st
from data.get_data import anual_pop_gender, neighborhood

st.title("Population and Unemployment in Barcelona")
st.text("Mid-Project Bootcamp CoreCodeSchool")

pob_gen = anual_pop_gender[0]
print(pob_gen)
st.selectbox("Age Range", [ne for ne in neigh])