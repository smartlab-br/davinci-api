''' Configuration loader for development environment '''
import os

#pylint: disable=R0903
class DevelopmentConfig():
    ''' Configuration handler '''
    GIT_MLREPO_BASE_URL = os.getenv('GIT_MLREPO_BASE_URL')
