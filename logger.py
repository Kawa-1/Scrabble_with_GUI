from __future__ import annotations
import logging
import os
import platform


def get_logger(name: __name__, level="INFO") -> logger:
    _path = ''
    if platform.system() == 'Darwin':
        _path = '{}{}'.format(os.getcwd(), '/DatabaseLogs/scrabble.log')
    elif platform.system() == 'Windows':
        _path = '{}{}'.format(os.getcwd(), '\\Logs\\scrabble.log')

    possible_logs = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
    level = level.upper()
    if level not in possible_logs:
        level = "INFO"

    logger = logging.getLogger(name)
    eval("logger.setLevel(logging.{})".format(level))

    file_handler = logging.FileHandler(_path)
    formatter = logging.Formatter("%(asctime)s LINE=%(lineno)d func_name=%(funcName)s | %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger