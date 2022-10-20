from distutils.debug import DEBUG

class DevelopmentConfig():
    DEBUG = True
# Parametros para la base de datos
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASS = 'Issac#corona'
    MYSQL_DB = 'test'

config = {
    'development': DevelopmentConfig
}


# Variables to configure
URL_A = "https://api.telegram.org/bot5119684311:AAE7FpjINWQ6WhIHEQoFRS_7y4pU4JQrqkU/getMe"
URL_B = "https://api.telegram.org/bot5119684311:AAE7FpjINWQ6WhIHEQoFRS_7y4pU4JQrqkU/getUpdates"
TOKEN = "5119684311:AAE7FpjINWQ6WhIHEQoFRS_7y4pU4JQrqkU"