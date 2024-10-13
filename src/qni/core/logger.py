import logging
import os

class Logger:
    def __init__(self):
        self.logger = logging.getLogger('qni_core')
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        self.file_handler = logging.FileHandler('qni_core.log')
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.stream_handler)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def set_log_level(self, level):
        self.logger.setLevel(getattr(logging, level))

    def remove_handlers(self):
        self.logger.removeHandler(self.file_handler)
        self.logger.removeHandler(self.stream_handler)
