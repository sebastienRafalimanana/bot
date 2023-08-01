
def create_app():
    """
    creation application flask
    :return instance application
    """
    from flask import Flask
    app = Flask(__name__)

    _configure_blueprints(app)

    return app
def _configure_blueprints(app):
    """
    configuration bot application
    :param app: instance application Flask
    """
    from bot import demo
    from bot import meteo

    blueprints = [
        demo,
        meteo
    ]
    for route in blueprints:
        app.register_blueprint(route)

