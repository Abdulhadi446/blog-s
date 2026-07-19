import os
from datetime import datetime

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SITE_CONFIG = {
        'name': os.environ.get('SITE_NAME', 'TechBlog'),
        'logo': '/static/images/logo.png',
        'description': os.environ.get('SITE_DESCRIPTION', 'Your go-to source for programming and technology insights'),
        'url': os.environ.get('SITE_URL', '/'),
        'author': os.environ.get('SITE_AUTHOR', 'TechBlog Team'),
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