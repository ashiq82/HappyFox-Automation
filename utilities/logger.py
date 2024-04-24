import inspect
import logging


def log():
    logger = logging.getLogger(inspect.stack()[1][3])
    logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    logger.setLevel(logging.INFO)
    return logger
