# -*- coding: utf-8 -*-
# %%
import joblib
import logging
from pathlib import Path
import os

from dynaconf import Dynaconf
import numpy as np
import pandas as pd


config = Dynaconf(settings_files=["settings.toml"])


def verify_data_type(df: pd.DataFrame, feature: str) -> str:
    """Return the data type of a given "feature".
    The data will be classified in "discrete" or "continuous".

    Arguments:
        df -- dataframe
        feature -- feature

    Returns:
        data type.
    """
    feature_type = df[feature].dtype

    if (feature_type == np.float64):
        data_type = 'continuous'
    elif (feature_type == np.int64) and (df[feature].nunique() > 10):
        data_type = 'continuous'
    else:
        data_type = 'discrete'

    return data_type

def load_dataprep_model(model_path: str) -> joblib:
    try:
        loaded_model = joblib.load(model_path)
        logger.debug(f'Model {Path(model_path).name} successfully loaded.')
        return loaded_model

    except FileNotFoundError:
        logger.error('File not found. Please verify the given path.')
        logger.info(
            f"""See the available models: {[x for x in Path(model_path).resolve().parent.glob('*.sav')]}"""
            )
        return None


def prepare_data(input_data: pd.DataFrame, model: joblib) -> pd.DataFrame:
    try:
        output_data = model.transform(input_data)
        logger.debug('Data successfully transformed.')
        return output_data
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    path = Path().absolute()

    if path.name == 'data':
        os.chdir(Path(__file__).resolve().parents[2])
        from src.custom_logger import get_logger

    log_file = os.environ.get('LOG_FILE')
    logger = get_logger(config.get('LOG_FILE'))

    loaded_model = load_dataprep_model(model_path='./models/dataprep_pipeline_4rd_experiment.sav')
