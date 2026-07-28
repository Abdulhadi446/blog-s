import os
from datetime import datetime

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SITE_CONFIG = {
        'name': os.environ.get('SITE_NAME', 'Trillioniar Blog'),
        'logo': '/static/images/logo.png',
        'description': os.environ.get('SITE_DESCRIPTION', 'Insights on AI, APIs, and developer tools from Trillioniar'),
        'url': os.environ.get('SITE_URL', '/'),
        'author': os.environ.get('SITE_AUTHOR', 'Trillioniar'),
        'current_year': datetime.now().year
    }

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}