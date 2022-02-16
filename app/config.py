import os
from dotenv import load_dotenv

# environmental variable configuration file
class Config(object):
    def init(self) -> None:
        # heavy performance loss, defaulting to false
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False

    # set config, defaults to prod config if no value found, config set in related function below
    def set_config(self):
        if True:
            self.local_config()
        else:
            self.prod_config()

    def prod_config(self):
        try:
            self.SECRET_KEY = os.environ.get('SECRET_KEY')
            self.SQLALCHEMY_DATABASE_URI = os.environ['SQL_DATABASE_URI']
        except Exception as er:
            print("SQLALCHEMY_DATABASE_URI failed!")

    def local_config(self):
        load_dotenv() # only needed to load .env locally
        try:
            self.SECRET_KEY = os.environ.get('SECRET_KEY')
            self.SQLALCHEMY_DATABASE_URI = os.environ['LOCAL_DB']
        except Exception as er:
           print("SQLALCHEMY_DATABASE_URI failed!")