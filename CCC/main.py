
import streamlit as st
st.title("Nammatha")

num1 = st.text_input("enter a number")
num2 = st.text_input("enter number 2")

if st.button ("Add"):
    st.title(int(num1)+int(num2))