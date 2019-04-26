import os

class BaseConfig(object):
	SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL']
	DEBUG=False
	TESTING=False

class DevelopmentConfig(BaseConfig):
	DEBUG=True
	TESTING=True

class TestingConfig(BaseConfig):
	DEBUG=False
	TESTING=True


		