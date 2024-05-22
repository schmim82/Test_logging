import pandas as pd
import streamlit as st



Rezepte_dataframe = pd.read_csv("test.csv", sep= ";")

st.markdown(Rezepte_dataframe)
