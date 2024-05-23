import streamlit as st

st.set_page_config(page_title="test")
st.title("test")

st.sidebar.title("test")

liste = ["1", "2"]

st.sidebar.radio("test", liste)
