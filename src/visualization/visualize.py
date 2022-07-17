# -*- coding: utf-8 -*-
# %%
import joblib
import logging
from pathlib import Path
import os

from dotenv import find_dotenv, dotenv_values
import pandas as pd
import plotly
import plotly.express as px


config = dotenv_values(find_dotenv())


def make_boxplot(df: pd.DataFrame, categorical: str, continuous: str, hue: str = None) -> plotly:
    try:
        fig = px.box(df, x=categorical, y=continuous, color=hue)
        fig.update_traces(quartilemethod="exclusive")
        return fig

    except FileNotFoundError as e:
        logger.error('File not found. Please verify the given path.')
        return None


if __name__ == '__main__':
    path = Path().absolute()
    
    if path.name == 'data':
        os.chdir(Path(__file__).resolve().parents[2])
    
    from src.custom_logger import get_logger

    log_file = config.get('LOG_FILE')
    logger = get_logger(config.get('LOG_FILE'))

