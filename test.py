import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

stock_df= pd.read_csv('stock_data.csv')

st.dataframe(stock_df)

stock_df = stock_df.iloc[1:100,]

chart = alt.Chart(stock_df).mark_line().encode(
    x='Date',
    y='Close'
)

st.altair_chart(chart,use_container_width=True)