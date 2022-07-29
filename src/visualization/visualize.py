# -*- coding: utf-8 -*-
# %%
from pathlib import Path
import os

from dynaconf import Dynaconf
import pandas as pd
import plotly
import plotly.express as px


config = Dynaconf(settings_files=["settings.toml"])


def make_boxplot(df: pd.DataFrame, categorical: str, continuous: str, hue: str = None) -> plotly:
    try:
        fig = px.box(df, x=categorical, y=continuous, color=hue)
        fig.update_traces(quartilemethod="exclusive")
        return fig

    except FileNotFoundError:
        logger.error('File not found. Please verify the given path.')
        return None


def make_violinplot(df: pd.DataFrame, categorical: str, continuous: str, hue: str = None) -> plotly:
    try:
        fig = px.violin(df, x=categorical, y=continuous, color=hue)
        return fig

    except FileNotFoundError:
        logger.error('File not found. Please verify the given path.')
        return None


def make_scatterplot(df: pd.DataFrame, categorical: str, continuous: str, hue: str = None) -> plotly:
    try:
        fig = px.scatter(df, x=categorical, y=continuous, color=hue)
        return fig

    except FileNotFoundError:
        logger.error('File not found. Please verify the given path.')
        return None


if __name__ == '__main__':
    path = Path().absolute()

    if path.name == 'data':
        os.chdir(Path(__file__).resolve().parents[2])

    from src.custom_logger import get_logger

    log_file = config.get('LOG_FILE')
    logger = get_logger(config.get('LOG_FILE'))


# %%
