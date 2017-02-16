import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '5bs5zIsG08A3P4hF1bDSVHiNO23z6qqO9qMm5xM/TX1hU3wUDWY6o2l0wWTifqWqsO3S1YV1voyE'
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = "jeffreiher@gmail.com"
    MAIL_PASSWORD = "j3ff_7797"
    # MAIL_DEFAULT_SENDER = '"Jeff Reiher" <jeff.reiher@seaturtleweb.com>'


class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False