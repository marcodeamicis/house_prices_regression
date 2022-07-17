# %%
import logging
import os
from time import asctime

from dotenv import find_dotenv, dotenv_values


config = dotenv_values(find_dotenv())

def get_logger(log_file: str = './log/file.log') -> logging.getLogger:

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(log_file)

    console_handler.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.ERROR)

    console_handler.setFormatter(logging.Formatter('%(levelname)-8s | %(filename)s:%(lineno)-4s | %(message)s'))
    file_handler.setFormatter(logging.Formatter('%(asctime)s; %(levelname)-s; %(filename)-s:%(lineno)-s; %(message)s', '%Y-%m-%d %H:%M'))

    if not logger.hasHandlers():
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger


if __name__ == '__main__':
    from pathlib import Path

    path = Path().absolute()
    
    if path.name == 'src':
        log_file = '../log/file.log'
    else:
        log_file = config.get('LOG_FILE')

    logger = get_logger(log_file)
    logger.debug('Executed.')
    logger.critical('Executed.')

    print(f"""Path: {path.name}
file_log: {log_file}""")

# %%
