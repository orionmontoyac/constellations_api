
"""[General Configuration Params]
"""


class Config(object):
    DEBUG = True
    SWAGGER = {
        'title': 'Flask Constellations API Docs',
    }
    PROPAGATE_EXCEPTIONS = True


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///constellations.sqlite3'


