import os
from dotenv import load_dotenv

load_dotenv()


class DevelopmentConfig:
    PORT = os.environ.get("PORT")
    DEBUG = True

class ProductionConfig:
    PORT = os.environ.get("PORT")
    DEBUG = False