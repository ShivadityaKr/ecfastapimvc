import os
from pathlib import Path
from configparser import ConfigParser
import environment
# Determine the directory containing the script
this_dir = Path(__file__).resolve().parent

# Specify the path to the properties.ini file
conf_dir = this_dir / 'properties.ini'

# Create a ConfigParser instance
parser = ConfigParser()

# Read the properties.ini file
parser.read(conf_dir, encoding='utf8')

parser['db']['DATABASE_URL'] = f"postgresql://{parser['db']['POSTGRES_USER']}:{parser['db']['POSTGRES_PASSWORD']}@{parser['db']['POSTGRES_SERVER']}:{parser['db']['POSTGRES_PORT']}/{parser['db']['POSTGRES_DB']}"

class Config:
    @staticmethod
    def read(section, property, default=None):
        return parser.get(section, property, fallback=default)

class Settings:
    PROJECT_NAME: str = Config.read('app', 'name')
    PROJECT_VERSION: str = "1.0.0"
    USE_SQLITE_DB: str = Config.read('db', 'USE_SQLITE_DB')
    POSTGRES_USER: str = Config.read('db', 'POSTGRES_USER')
    POSTGRES_PASSWORD = Config.read('db', 'POSTGRES_PASSWORD')
    POSTGRES_SERVER: str = Config.read('db', 'POSTGRES_SERVER')
    POSTGRES_PORT: str = Config.read('db', 'POSTGRES_PORT')
    POSTGRES_DB: str = Config.read('db', 'POSTGRES_DB')
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()