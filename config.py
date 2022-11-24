import os


class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dSW@l@oh4F4@3lDjv@9*mJ5j#A$B58iT#@cxHNJ#@"
