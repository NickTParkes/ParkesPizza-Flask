from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from app.config import Config
from flask_login import LoginManager
from dotenv import load_dotenv

#initialize Flask App
app = Flask(__name__)
#initialize login object 
login = LoginManager(app)
login.login_view = 'login' 

#configure app via _config
_config = Config()
_config.set_config()
app.config.from_object(_config)

#initialize db
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes , models