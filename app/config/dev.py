import os

class DevelopmentConfig(object):
    GIT_MLREPO_BASE_URL = os.getenv('GIT_MLREPO_BASE_URL')
