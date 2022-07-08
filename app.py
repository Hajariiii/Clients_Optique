
import string
from numpy import double, int64, number
from sqlalchemy import Numeric
import streamlit as st
import pandas as pd
import datetime

st.title("Mes Clients For You Optique")

df = pd.read_csv(r"ClientsT.csv")
st.write(df)
# st.write("Streamlit version:", st.__version__)

with st.sidebar:
    st.header("Options")
    #options_form = st.form("options_form")
    with st.form(key = 'Options'):
    
         user_lastname = st.text_input("Nom")
         user_firstname = st.text_input("Prénom")
         user_lod = st.text_input("Vision loin OD")
         user_log = st.text_input("Vision loin OG")
         user_pod = st.text_input("Vision Proche OD")
         user_pog = st.text_input("Vision Proche OG")
         addictions = st.text_input("Additions")
         Avance = st.text_input("Avance")
         Cadre = st.text_input("Cadre")
         Prix_t = st.text_input("Prix Total")
         Date = st.text_input("Date")
         Téléphone = st.text_input("Téléphone")

         add_data = st.form_submit_button()
if add_data:
    #st.write(user_lastname,user_firstname,user_lod,user_log,user_pod,user_pog,addictions,Avance,Cadre,Prix_t,Date,Téléphone)
    new_data = {"Nom":user_lastname,
    "Prénom" :user_firstname,
    "Vision loin OD":user_lod,
    "Vision loin OG":user_log,
    "Vision Proche OD":user_pod,
    "Vision Proche OG":user_pog,
    "Additions":addictions,
    "Avance":Avance,
    "Cadre":Cadre,
    "Prix Total":Prix_t,
    "Date":Date,
    "Téléphone":int(Téléphone)}
            
    df = df.append(new_data, ignore_index=True)
    st.header("Dataset version :",datetime.datetime.today() )
    st.write(df)
    #df.to_csv(r"ClientsT.csv", index = False)
