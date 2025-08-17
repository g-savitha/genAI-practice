import streamlit as st
import pandas as pd

st.title('streamlit text input')

name = st.text_input('enter your name')
age = st.slider('select your age', 0, 100, 25)

st.write(f'your age is {age}')
if name:
    st.write(f'hello {name}')

options = ["python", "javascript", "c++", "java"]
choice = st.selectbox('choose your fav lang', options)

st.write(f'you have selected {choice}')

data = {
    "name": ['john', 'jacob', 'jill'],
    "age": [20, 25, 26],
    "city": ['new york', 'london', 'delhi']
}

df = pd.DataFrame(data)
df.to_csv('sampledata.csv')
st.write(df)

uploaded_file = st.file_uploader('choose a csv file', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
