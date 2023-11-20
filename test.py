import pandas as pd
import streamlit as st

stock_df= pd.read_csv('stock_data.csv')

st.dataframe(stock_df)