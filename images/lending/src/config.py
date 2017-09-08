# -*- coding: utf-8 -*-

import os
import logging
from logging.handlers import RotatingFileHandler

# ...
class ImproperlyConfigured(Exception):
    pass

# ...
def get_env_variable(var_name, allow_none=False):
    try:
        return os.environ[var_name]
    except KeyError:
        if allow_none is False:
            err_msg = "Set the %s environment variable" % var_name
            raise ImproperlyConfigured(err_msg)
        return None




class BaseConfig(object):
    DEBUG = False
    TESTING = False

    # ...dir
    PROJECT_PATH = os.path.dirname(
        os.path.abspath(__file__)
    )
    
    # ...templates
    TEMPLATE_FOLDER = os.path.join(
        PROJECT_PATH, 'templates'
    )

    # ..kyes
    SECRET_KEY = '1d94e52c-1c89-4515-b87a-f48cf3cb7f0b'


    # ..logs
    # LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_FORMAT = (
        '%(asctime)s [%(levelname)s]: %(message)s ',
        '%Y-%m-%d %H:%M:%S'        
    )
    LOGGING_LOCATION = os.path.join(
        PROJECT_PATH, '.logs/lending.log'
    )
    LOGGING_SIZE = 52428800  
    LOGGING_LEVEL = logging.INFO


    # ...
    RUNNING_HOST = get_env_variable('RUNNING_HOST','0.0.0.0')
    RUNNING_PORT = get_env_variable('RUNNING_PORT','8000')


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite://'    
    SECRET_KEY = 'a9eec0e0-23b7-4788-9a92-318347b9a39f'

    # ...static
    STATIC_FOLDER = os.path.join(
        BaseConfig.PROJECT_PATH, 'static'
    )
    # ...
    LOGGING_LEVEL = logging.DEBUG

class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SECRET_KEY = '792842bc-c4df-4de1-9177-d5207bd9faa6'

config = {
    "base": "config.BaseConfig",
    "development": "config.DevelopmentConfig",
    "testing": "config.TestingConfig",
}


def init_app(app):
    # ...
    config_name = os.getenv('FLASK_CONFIGURATION', 'base')
    app.config.from_object(config[config_name])

    # logging
    # ...
    formatter = logging.Formatter(*app.config['LOGGING_FORMAT'])
    handler = RotatingFileHandler(
        app.config['LOGGING_LOCATION']
        , maxBytes = app.config['LOGGING_SIZE']
        , backupCount = 5)
    # ...
    handler.setLevel(app.config['LOGGING_LEVEL'])
    handler.setFormatter(formatter)    
    app.logger.addHandler(handler)

    # ..templates
    template_folder = app.config.get('TEMPLATE_FOLDER',None)
    if template_folder:
        app.template_folder = template_folder

    # ..static
    static_folder = app.config.get('STATIC_FOLDER',None)
    if static_folder:
        app.static_folder = static_folder