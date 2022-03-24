from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from mysqlx import Auth
from routes.auth import auth
from utils.db import db

app = Flask(__name__)
app.register_blueprint(auth)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)


