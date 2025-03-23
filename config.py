import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')  # Replace with a secure secret key
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Example SQLite database URI (can be changed for production databases)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///hbnb_evolution.db')

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    """Production configuration."""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # Ensure to set it in production
    DEBUG = False
    ENV = 'production'
