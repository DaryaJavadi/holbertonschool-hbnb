from flask import Flask
from flask_restx import Api
from app.part2.api.v1 import api_bp 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Update with your actual database URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['ENV'] = 'development'

    db.init_app(app)
    
    # Register API
    app.register_blueprint(api_bp, url_prefix="/api/v1")
    migrate.init_app(app, db)
    return app
