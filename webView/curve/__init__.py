from flask import Blueprint
from mainapp import db,bootstrap

curves = Blueprint("cy",__name__,template_folder="templates",static_folder='static',
	static_url_path='/curve/static')

from curve import views