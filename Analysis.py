import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
st.set_page_config(layout="wide",page_title="India Analysis")
data=pd.read_csv("india.csv")
base="light"
primaryColor="red"
data.rename(columns={"Households_with_Internet":"Households with Internet"},inplace=True)
data["Sex Ratio per 1000 males"]=round(data["Sex Ratio per 1000 males"],0)
data["Sex Ratio per 1000 males"]=data["Sex Ratio per 1000 males"].astype(int)
st.sidebar.title("Geographical Analyis")
x=sorted(data["State"].unique())
x.insert(0,"Overall")
state=st.sidebar.selectbox("Select a state",x)
cols=["Population","Households with Internet","Sex Ratio per 1000 males","Literacy Rate"]
df=data[cols]
primary=st.sidebar.selectbox("Select primary factor",sorted(df.columns))
secondary=st.sidebar.selectbox("Select secondary factor",sorted(df.columns))
btn=st.sidebar.button("Plot a graph")
if btn:
    st.markdown(f'<div style="text-align: center; color: red;"><h1>{state}</h1></div>', unsafe_allow_html=True)
    if state=="Overall":

        fig = px.scatter_mapbox(data, lat="Latitude", lon="Longitude",size=primary,color=secondary,hover_data="District", zoom=3,mapbox_style="carto-positron",width=1500,height=700)
        st.plotly_chart(fig)
    else:
        states=data[data["State"]==state]
        fig = px.scatter_mapbox(states, lat="Latitude", lon="Longitude", size=primary, color=secondary,
                                hover_data="District", zoom=6, mapbox_style="carto-positron",color_continuous_scale=px.colors.cyclical.IceFire, width=1500, height=700,)
        st.plotly_chart(fig)