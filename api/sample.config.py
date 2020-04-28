""" Config classes for Environments
"""
import os

class AppConfig(object):
    # Flask settings
    SERVER_NAME = 'api.otrrent.app-workshop.de'
    SECRET_KEY = 'donotpopulateanysecrets'
    DEBUG = False  # Do not use debug mode in production
    TESTING = False
    PREFERRED_URL_SCHEME = 'https'

    # SQLAlchemy settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):         # Note: all caps
        self.DB_SERVER = os.environ.get('MYSQL_SERVER')
        self.DB_USER = os.environ.get('MYSQL_ROOT_USER')
        self.DB_PASSWORD = os.environ.get('MYSQL_ROOT_PASSWORD')

        return 'mysql+pymysql://{}:{}@{}/otrrent'.format(self.DB_USER, self.DB_PASSWORD, self.DB_SERVER)

class ProductionConfig(AppConfig):
    pass

class TestingConfig(AppConfig):
    TESTING = False

class DevelopmentConfig(AppConfig):
    DEBUG = True
    SECRET_KEY = 'oahwhatasecret'
    SQLALCHEMY_ECHO = True
    SERVER_NAME = None
    PREFERRED_URL_SCHEME = None


""" HTTP Authentification  """
authorizations = {
    'basicauth': {
        'type': 'basic',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}
