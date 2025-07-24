import streamlit as st
import pandas as pd

st.title("THIS IS NEW APPLICATION")

name=st.text_input("Enter the name")
if name:
    st.write(f"your have been selected {name}")
    st.balloons()
    st.snow()


money=st.slider("select your money you want ",0,100,20)
st.write(f"you have {money} money in account")

options=["java","c++","python","javascript","YAML"]
x=st.selectbox("choose the fav coding language",options)
st.write(x)

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df=pd.DataFrame(data)
st.write(df)


