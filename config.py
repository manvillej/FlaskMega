import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '8vd%4la%7TuP5Od3vG6DDaxTuU6X%U%aGRbiS6Xb'