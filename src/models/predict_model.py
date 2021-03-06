# -*- coding: utf-8 -*-
# %%
import joblib
import logging
from pathlib import Path
import os

from dynaconf import Dynaconf
import pandas as pd


config = Dynaconf(settings_files=["settings.toml"])


def load_predicting_model(model_path: str) -> joblib:
    try:
        loaded_model = joblib.load(model_path)
        logger.debug(f'Model {Path(model_path).name} successfully loaded.')
        return loaded_model

    except FileNotFoundError as e:
        logger.error('File not found. Please verify the given path.')
        logger.info(
            f"""See the available models: {[x for x in Path(model_path).resolve().parent.glob('*.sav')]}"""
            )
        return None

def predict(input_data: pd.DataFrame, model: joblib) -> pd.DataFrame:
    try:
        output_data = model.predict(input_data)
        logger.debug(f'Prediction successfully done.')
        return output_data
    except Exception as e:
        logger.error(f"An error occured while doing 'predict': {e}")


if __name__ == '__main__':
    path = Path().absolute()
    
    if path.name == 'models':
        os.chdir(Path(__file__).resolve().parents[2])
        from src.custom_logger import get_logger

    log_file = os.environ.get('LOG_FILE')
    logger = get_logger(config.get('LOG_FILE'))

    loaded_model = load_predicting_model(model_path='./models/model_7th_experiment_7th_experiment_gridsearch.sav')
