
class Config(object):
    """Configuration de l'application"""
    from dotenv import load_dotenv
    from os import environ
    load_dotenv()

    #: Flask configuration
    APP_PORT = int(environ.get('APP_PORT', 8011))
    APP_HOST = environ.get('APP_HOST', 'localhost')
    APP_NAME = "Messenger Boot"

