# -*- coding: utf-8 -*-
# %%
import joblib
import logging
from pathlib import Path
import os

from dotenv import find_dotenv, dotenv_values
import pandas as pd

config = dotenv_values(find_dotenv())


def load_dataprep_model(model_path: str) -> joblib:
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

def prepare_data(input_data: pd.DataFrame, model: joblib) -> pd.DataFrame:
    try:
        output_data = model.transform(input_data)
        logger.debug(f'Data successfully transformed.')
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
