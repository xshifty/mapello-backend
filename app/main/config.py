import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    TESTING = False
    DEBUG = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = True

configs = {
    'prod': ProductionConfig,
    'dev': DevelopmentConfig,
    'test': TestingConfig,
}
