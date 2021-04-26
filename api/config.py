import os
from dotenv import load_dotenv

load_dotenv()


class DevelopmentConfig:
    PORT = os.environ.get("PORT")
    DEBUG = True
    COM_PORT = os.environ.get('COM_PORT')

class ProductionConfig:
    PORT = os.environ.get("PORT")
    DEBUG = False
    COM_PORT = os.environ.get('COM_PORT')