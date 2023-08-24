
class Config(object):
    """Configuration de l'application"""
    from dotenv import load_dotenv
    from os import environ
    load_dotenv()

    #: Flask configuration
    APP_NAME = "Messenger Boot"
    APP_PORT = int(environ.get('APP_PORT', 8011))
    APP_HOST = environ.get('APP_HOST', 'localhost')

    #: Facebook configuration
    ACCESS_TOKEN = 'EAAEz0EkBmL4BOw5DpEeIgZChb3KE6PYugIBLNotQv10Fg8qSKsaaKjuOqTgj2ERFl1xZA9KJcbgfZABQ8U7jj13vKHP9zjWBAp9MZA7AxfwoqqKOUI5IvH94bpD5NE3gJmlKAfj3oUZAlHxxPDlvPqkiVEaSTQ92HdSKHOsCWw2uUOvVBMYfTCTTn9ZACBkwkx'
    VERIFY_TOKEN = '2kl73mjy1e'
    URL_API = "https://script.google.com/macros/s/AKfycbxFiSA9E-gVqJviFKh8B86l8e9Pa6KHIjNGHe0xYSmhnDARBbxlZm9C-FcF3W6vYwGN/exec?region="

    #: Contexte path configuration
    CONTEXTE_PATH = environ.get('CONTEXTE_PATH', '/webhook')

    #: Loggin
    MESSAGE_LOGIN = f"*: STARTING BOT SERVER on {APP_PORT}"

    #: DATE
    PASS_DATE = "01/01/01"

