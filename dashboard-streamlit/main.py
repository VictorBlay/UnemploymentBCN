import streamlit as st
from data.get_data import anual_pop

st.title("Population and Unemployment in Barcelona")
st.text("Mid-Project Bootcamp CoreCodeSchool")
st.selectbox("Neighbourhood Select", anual_pop)