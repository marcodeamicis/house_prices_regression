# %%
from tkinter import EXCEPTION
from dotenv import find_dotenv, dotenv_values
import pandas as pd
import streamlit as st

from src.custom_logger import get_logger
from src.visualization.visualize import make_boxplot


config = dotenv_values(find_dotenv())

logger = get_logger(config.get('LOG_FILE', './log/file.log'))

try:
    x_train = pd.read_parquet(
        config.get('INTERIM_FOLDER', './data/interim/') + \
        config.get('X_TRAIN', 'X_train_3rd_dataprep.pqt'))
    logger.debug('x_train loaded')
except EXCEPTION as e:
    logger.error('Error during X_train loading.')

# %%
msg_sidebar = """
> This streamlit app is just a POC using the
> [Kaggle's House Prediction Challenge](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques).
"""

with st.sidebar:
    st.title('House Prediction Challenge')

    # btn_home = st.button('Home')
    btn_data_exploration = st.button('Data Exploration', help='Asseing the data.')
    btn_predicting = st.button('Predicting SalePrice', help='Predict a SalePrice.')

    st.markdown(msg_sidebar)

# TODO: I deactivated this part while we are working on the other parts.
# if btn_home:
#     btn_predicting = btn_data_exploration = False
#     with st.container():
#         main_title = st.title('Principal')

if btn_data_exploration:
    btn_predicting = btn_home = False
    with st.container():
        main_title = st.title('Data Exploration')
        st.plotly_chart(make_boxplot(df=x_train, categorical='YrSold', continuous='GrLivArea', hue='CentralAir_Y'))

elif btn_predicting:
    btn_data_exploration = btn_home = False
    with st.container():
        main_title = st.title('Predicting')
