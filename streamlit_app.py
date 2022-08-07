from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
st.title("Streamlit Test")
df = pd.read_csv('./STCS_체감온도.csv', encoding='cp949')
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)
    
st.subheader('날짜별 체감온도')
option = st.selectbox(
    'Select Line', 
    (df['일자']))

data = df.loc[(df['일자'] == option)] 
st.write(data)
