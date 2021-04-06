class Config:

    DEBUG = False
    TESTING = False
    

class StagingConfig(Config):

    DEBUG = True
    TYPE='Tester'
  


class DevConfig(Config):

    DEBUG = False
    TYPE='Developer'
    