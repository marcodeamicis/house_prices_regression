# -*- coding: utf-8 -*-
# %%
import logging
from pathlib import Path
import os

from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())

def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


if __name__ == '__main__':
    path = Path().absolute()
    
    if path.name == 'data':
        os.chdir(Path(__file__).resolve().parents[2])
        from src.custom_logger import get_logger

    log_file = os.environ.get('LOG_FILE')

    logger = get_logger(os.environ.get('LOG_FILE'))
# %%
