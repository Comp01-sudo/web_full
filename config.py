from flask import Config

class DevelopmentConfig(Config):
  DEBUG = True
  SECRET_KEY = "wsedfAIUBOLKyfskyeasefo87324twregqia"
  BCRYPT_LOG_ROUNDS = 12
  SQLALCHEMY_DATABASE_URI = 'sqlite:////server/db.db'

class ProductionConfig(Config):
  DEBUG = False
  SECRET_KEY = 'skjrvhgfuaksryfvaksuroiw74rtwgkesjfhdbcioe8yrgbvf'
  BCRYPT_LOG_ROUNDS = 37