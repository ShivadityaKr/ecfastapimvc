import logging
import sys
import os
from logging.handlers import RotatingFileHandler
from utils.config import Config
from environment import router

class Logger():
    CONFIG_KEY = 'log'
    LOG_FILE_SIZE = 1 * 1024 * 1024  # 1MB in bytes

    @staticmethod
    def get_level():
        # MARK: - Default
        return Config.read(Logger.CONFIG_KEY, 'level')

    @staticmethod
    def get_filename():
        return Config.read(Logger.CONFIG_KEY, 'filename')

    @staticmethod
    def get_format():
        return Config.read(Logger.CONFIG_KEY, 'format')

    @staticmethod
    def get_date_format():
        return Config.read(Logger.CONFIG_KEY, 'dateformat')

    @staticmethod
    def get_logger(name):
        logger = logging.getLogger(name)
        logger.setLevel(Logger.get_level())

        formatter = logging.Formatter(
            Logger.get_format(),
            Logger.get_date_format())

        # Add a stream handler to print logs to console
        stream_hdlr = logging.StreamHandler(sys.stdout)
        stream_hdlr.setFormatter(formatter)
        logger.addHandler(hdlr=stream_hdlr)

        # Add a rotating file handler to save logs to a file and rotate based on file size
        file_hdlr = RotatingFileHandler(
            filename=Logger.get_filename(),
            maxBytes=Logger.LOG_FILE_SIZE,
            backupCount=5  # Number of backup files to keep
        )
        file_hdlr.setFormatter(formatter)
        logger.addHandler(hdlr=file_hdlr)

        return logger
