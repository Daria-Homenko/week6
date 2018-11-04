import os


class Config:
    TEST_VARIABLE = "Config"
    SECRET_KEY = 'b\xaa;\x0b\x12\x8a\xa1V+\x16\xc5'
    PG_USER = "daria"
    PG_PASSWORD = "1"
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "cursor_flask_lesson"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    TEST_VARIABLE = "Dev Config"
    SECRET_KEY = os.urandom(16)


class TestConfig(Config):
    TEST_VARIABLE = "Test Config"
    SECRET_KEY = 'b\xaa;\x0b\x12'


def runtime_config():
    env = os.environ.get("ENV")
    if env == "DEV":
        return DevConfig
    if env == "TEST":
        return TestConfig
    else:
        return Config
