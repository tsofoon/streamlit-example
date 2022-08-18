from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Welcome to Streamlit!


def load_data():
    st_data = pd.read_csv('fake_streamlit_data.csv')
    return st_data

df = load_data()

col_chosen = st.selectbox('Pick one', list(df.columns))

tmp = pd.DataFrame(df.groupby(col_chosen).nunique().sort_values(by = 'user_id', ascending = False)['user_id']).head(15)
tmp.plot.bar()
if col_chosen =='name':
    plt.title('Top 15 used streamlit componet by active user')
else:
    title = 'Top 15 ', col_chosen,' by active user'
    plt.title(title)
    
