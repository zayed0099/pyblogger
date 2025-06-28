import os
from flask import Flask 
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
	app = Flask(__name__)

	from .auth import auth as auth_bp
	from .main import main as main_bp
	from .dashboard import dashboard as dashboard_bp
	
	app.register_blueprint(auth_bp, url_prefix='/auth')
	app.register_blueprint(main_bp)
	app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

	return app