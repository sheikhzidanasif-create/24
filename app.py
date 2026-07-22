import streamlit as st
import pandas as pd
import numpy as np

st.title('My First Streamlit App')

st.write("Hello, world! This is a simple Streamlit application.")

data = pd.DataFrame({
    'col1': [1, 2, 3],
    'col2': [10, 20, 30]
})

st.write("Here's some data:")
st.dataframe(data)
