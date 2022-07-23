# %%
from dynaconf import Dynaconf
import numpy as np
import pandas as pd
import streamlit as st

from src.custom_logger import get_logger
from src.data.make_dataprep import verify_data_type
from src.visualization.visualize import make_boxplot, make_scatterplot, make_violinplot


config = Dynaconf(settings_files=["settings.toml"])

logger = get_logger(config.get('LOG_FILE', './log/file.log'))

try:
    x_train = pd.read_parquet(
        config.get('INTERIM_FOLDER', './data/interim/') + \
        config.get('X_TRAIN', 'X_train_3rd_dataprep.pqt'))
    y_train = pd.read_parquet(
        config.get('INTERIM_FOLDER', './data/interim/') + \
        config.get('Y_TRAIN', 'y_train_3rd_dataprep.pqt'))
    df = pd.concat([x_train, y_train], axis=1)
    logger.debug('x_train loaded')
except:
    logger.error('Error during X_train loading.')

# %%
msg_sidebar = """
> This streamlit app is just a POC using the
> [Kaggle's House Prediction Challenge](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques).
"""

with st.sidebar:
    st.title('House Prediction Challenge')

    option = st.radio(
        'Choose one option:',
        ['Data Exploration', 'Predicting SalePrice']
    )

    st.markdown(msg_sidebar)

if option == 'Data Exploration':
    with st.container():
        main_title = st.title('Data Exploration')

        x_axis = st.selectbox('X axis:', (df.columns.tolist()))
        y_axis = st.selectbox('Y axis:', (df.columns.tolist()))
        hue = st.selectbox('hue:', (df.columns.tolist()))

        x_type = verify_data_type(df=df, feature=x_axis)
        y_type = verify_data_type(df=df, feature=y_axis)

        if (x_type == 'continuous') and (y_type == 'continuous'):
            lst_graph = ['scatter', ]
        elif (x_type == 'discrete') and (y_type == 'continuous'):
            lst_graph = ['boxplot', 'violinplot', ]
        else:
            lst_graph = ['teste', 'teste2', ]

        graph_selection = st.selectbox('Select a graph:', lst_graph)

        if graph_selection == 'boxplot':
            st.plotly_chart(make_boxplot(df=df, categorical=x_axis, continuous=y_axis, hue=hue))
        elif graph_selection == 'violinplot':
            st.plotly_chart(make_violinplot(df=df, categorical=x_axis, continuous=y_axis, hue=hue))
        elif graph_selection == 'scatter':
            st.plotly_chart(make_scatterplot(df=df, categorical=x_axis, continuous=y_axis, hue=hue))
        else:
            st.write('Other graph.')

elif option == 'Predicting SalePrice':
    btn_data_exploration = btn_home = False
    with st.container():
        main_title = st.title('Predicting')
