import streamlit as st
import pandas as pd
import numpy as np

# title

st.title('hello')

st.write('this is a simple text')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# display data frame

st.write(df)
st.write('here is the data frame')

# create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
