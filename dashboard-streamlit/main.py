from turtle import width
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import seaborn as sns
from data.get_data import years, genero, años, anual_pop_gender, neighborhood, anual_pop, unemploy_gender, unemploy_neigh, unemploy_demand, meses

gender = genero()
gender_ = [g for g in gender.values()][0]
año = años()
año_ = [a for a in año.values()][0]
mes = meses()
mes_ = [m for m in mes.values()][0]
year = years()
year_ = [m for m in year.values()][0]

st.markdown("<h1 style='text-align: center; color: black;'>Population and Unemployment in Barcelona</h1>", unsafe_allow_html=True)
st.write("**Mid-Project Bootcamp (Big Data and Machine Learning) in CoreCodeSchool.**")
st.image("barcelona.jpg")


st.sidebar.header("Selectors for Population Information")
sel_año = st.sidebar.selectbox("Year Selector",año_)
sel_gender = st.sidebar.selectbox("Gender Selector", gender_)

col1, col2 = st.columns(2)

df = pd.DataFrame.from_dict(anual_pop_gender(sel_año, sel_gender), orient="index")
df = df.rename({0: "Population"}, axis="columns")
df.reset_index(inplace=True)
df = df.rename(columns= {"index":"Age"})
col1.write("**Population filtered by selectors**")
col1.write(df)

p = alt.Chart(df).mark_bar().encode(
    x="Age",
    y="Population"
)
p = p.properties(
    width=alt.Step(15)
)
col2.write("**Bar chart from selectors**")
col2.write(p)

labels = anual_pop_gender(sel_año, sel_gender).keys()
sizes = anual_pop_gender(sel_año, sel_gender).values()

fig = px.pie(df, values = "Population", names = "Age")
fig.update_layout(showlegend=False)
col1.write(fig)

st.sidebar.header("Selectors for Unemployment Information")
sel_año = st.sidebar.selectbox("Year Selector",mes_)
sel_gender = st.sidebar.selectbox("Gender Selector", year_)