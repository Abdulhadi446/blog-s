import os
from datetime import datetime

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SITE_CONFIG = {
        'name': os.environ.get('SITE_NAME', 'Trillioniar Blog'),
        'logo': '/static/favicon.svg',
        'description': os.environ.get('SITE_DESCRIPTION', 'Daily AI news, a weekly AI news roundup every Monday and a monthly AI news recap on the first — AI models, agents, chips and policy, explained.'),
        'url': os.environ.get('SITE_URL', '/'),
        'author': os.environ.get('SITE_AUTHOR', 'Trillioniar'),
        'current_year': datetime.now().year,
        # Optional integrations. Leave unset to keep the site dependency-free.
        'newsletter_url': os.environ.get('NEWSLETTER_URL', ''),
        'twitter_handle': os.environ.get('TWITTER_HANDLE', ''),
        'google_site_verification': os.environ.get('GOOGLE_SITE_VERIFICATION', ''),
        'plausible_domain': os.environ.get('PLAUSIBLE_DOMAIN', ''),
    }

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    PREFERRED_URL_SCHEME = 'https'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}