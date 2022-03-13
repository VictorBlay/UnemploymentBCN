from turtle import width
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from data.get_data import years, genero, años, anual_pop_gender, anual_pop_neigh, unemploy_gender, unemploy_neigh, unemploy_demand, meses

page = st.sidebar.selectbox('Select page', ['Population data','Unemployment data'])

if page == 'Population data':
    gender = genero()
    gender_ = [g for g in gender.values()][0]
    año = años()
    año_ = [a for a in año.values()][0]

    st.markdown("<h1 style='text-align: center; color: black;'>Population in Barcelona</h1>", unsafe_allow_html=True)
    st.write("**Mid-Project Bootcamp (Big Data and Machine Learning) in CoreCodeSchool.**")
    st.image("barcelona.jpg")

    sel_año = st.selectbox("Year selector",año_)
    sel_gender = st.selectbox("Gender selector", gender_)

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

    fig = px.pie(df, values = "Population", names = "Age")
    fig.update_layout(showlegend=False)
    col1.write(fig)
    
else:
    st.markdown("<h1 style='text-align: center; color: black;'>Unemployment in Barcelona</h1>", unsafe_allow_html=True)
    st.write("**Mid-Project Bootcamp (Big Data and Machine Learning) in CoreCodeSchool.**")
    st.image("barcelona.jpg")

    mes = meses()
    mes_ = [m for m in mes.values()][0]
    year = years()
    year_ = [m for m in year.values()][0]

    sel_year = st.selectbox("Year selector",year_)
    sel_mes = st.selectbox("Month selector",mes_)

    df_ = pd.DataFrame.from_dict(unemploy_neigh(sel_year, sel_mes), orient="index")
    df_ = df_.rename({0: "Unemployment"}, axis="columns")
    df_.reset_index(inplace=True)
    df_ = df_.rename(columns= {"index":"Neighborhood"})
    st.write("**Unemployment filtered by selectors**")
    st.write(df_)

    b = alt.Chart(df_).mark_bar(size=5).encode(
        x="Neighborhood",
        y="Unemployment"
    )
    b = b.properties(
        width=alt.Step(9)
    )
    st.write("**Bar chart from selectors**")
    st.write(b)

    df_g = pd.DataFrame.from_dict(unemploy_gender(sel_year, sel_mes), orient="index")
    df_g = df_g.rename({0: "Unemployment"}, axis="columns")
    df_g.reset_index(inplace=True)
    df_g = df_g.rename(columns= {"index":"Gender"})

    fig = px.pie(df_g, values = "Unemployment", names = "Gender")
    fig.update_layout(showlegend=False)
    st.write(fig)

    df_u = pd.DataFrame.from_dict(unemploy_demand(sel_year, sel_mes), orient="index")
    df_u = df_u.rename({0: "Unemployment"}, axis="columns")
    df_u.reset_index(inplace=True)
    df_u = df_u.rename(columns= {"index":"Demand"})

    fig = px.pie(df_u, values = "Unemployment", names = "Demand")
    fig.update_layout(showlegend=False)
    st.write(fig)