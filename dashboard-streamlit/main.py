from turtle import width
import streamlit as st
import pandas as pd
import altair as alt
from data.get_data import años, anual_pop_gender, neighborhood, anual_pop, unemploy_gender, unemploy_neigh, unemploy_demand, meses

year = "2015"
gender = "Male"
barrios = []
for i in neighborhood():
    for b in i:
        barrios.append(b)

st.markdown("<h1 style='text-align: center; color: black;'>Population and Unemployment in Barcelona</h1>", unsafe_allow_html=True)
st.image("barcelona.jpg")
st.text("Mid-Project Bootcamp CoreCodeSchool")

st.subheader("1. Year Selector")
st.selectbox("Year Selector",barrios)

col1, col2 = st.columns(2)

df = pd.DataFrame.from_dict(anual_pop_gender(year, gender), orient="index")
df = df.rename({0: "count"}, axis="columns")
df.reset_index(inplace=True)
df = df.rename(columns= {"index":"Age"})
col1.write("2. Gender Population")
col1.write(df)

p = alt.Chart(df).mark_bar().encode(
    x="Age",
    y="count"
)
p = p.properties(
    width=alt.Step(15)
)
col2.write("3. Bar chart")
col2.write(p)