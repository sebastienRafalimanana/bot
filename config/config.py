
class Config(object):
    """Configuration de l'application"""
    from dotenv import load_dotenv
    from os import environ
    load_dotenv()

    #: Flask configuration
    APP_PORT = int(environ.get('APP_PORT', 8011))
    APP_HOST = environ.get('APP_HOST', 'localhost')
    APP_NAME = "Messenger Boot"

    #: Facebook configuration

    ACCESS_TOKEN = 'EAAEz0EkBmL4BOw5DpEeIgZChb3KE6PYugIBLNotQv10Fg8qSKsaaKjuOqTgj2ERFl1xZA9KJcbgfZABQ8U7jj13vKHP9zjWBAp9MZA7AxfwoqqKOUI5IvH94bpD5NE3gJmlKAfj3oUZAlHxxPDlvPqkiVEaSTQ92HdSKHOsCWw2uUOvVBMYfTCTTn9ZACBkwkx'
    VERIFY_TOKEN = '2kl73mjy1e'
    URL_API = "https://script.google.com/macros/s/AKfycbyZSQKPKKmkJ7lbspDbro263T0RkaBQOffe4_TEG0IrZP77mN-q5oFTNtnxgFZ5VISX/exec?region="

    #: Contexte path configuration
    CONTEXTE_PATH = environ.get('CONTEXTE_PATH', '/webhook')

    #: Loggin
    MESSAGE_LOGIN =f"*: STARTING BOT SERVER on {APP_PORT}"

    #: Google analytics

    G_GLOBAL_TAG = """
    <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-GZ27XX4HJL"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-GZ27XX4HJL');
        </script>
    """

