from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = "hellowkeys"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+base_dir+"/data.db"

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

from curve import curves as curve_blue

app.register_blueprint(curve_blue)
