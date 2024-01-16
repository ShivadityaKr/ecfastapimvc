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

# Get the value of the 'env' key from the 'app' section
env_value = parser.get('app', 'env')

selected_env_file  = environment.dev

if env_value == "DEV":
    selected_env_file  = environment.dev

# Load environment variables from the selected file
with open(selected_env_file) as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):  # Skip empty lines and comments
            key, value = line.split('=')
            key = key.strip()
            value = value.strip()
            os.environ[key] = value

class Settings:
    PROJECT_NAME: str = Config.read('app', 'name')
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_API_DOCS: str = Config.read('app', 'api-docs.path') 
    USE_SQLITE_DB: str = os.environ['USE_SQLITE_DB']
    POSTGRES_USER: str = os.environ['POSTGRES_USER']
    POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
    POSTGRES_SERVER: str = os.environ['POSTGRES_SERVER']
    POSTGRES_PORT: str = os.environ['POSTGRES_PORT']
    POSTGRES_DB: str = os.environ['POSTGRES_DB']
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()

