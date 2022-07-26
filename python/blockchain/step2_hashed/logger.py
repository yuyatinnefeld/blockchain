import logging
import time


FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")

root_logger = logging.getLogger()
console_handler = logging.StreamHandler()
console_handler.setFormatter(FORMATTER)
root_logger.addHandler(console_handler)
root_logger.setLevel(logging.DEBUG)

def get_logger():
    return root_logger

