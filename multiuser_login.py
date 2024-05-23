import streamlit as st

st.set_page_config(page_title="test")
st.title("test")

st.sidebar.title("test")




button = st.sidebar.button("drücken")


if button:
  liste = ["2"]

else:
  liste = ["1", "2"]
  
st.sidebar.radio("test", liste)
