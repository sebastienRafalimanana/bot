from flask import Flask
from education.webhook import education
from demo.webhook import wealther

app = Flask(__name__)

#Enregistrement de l'application dans l'application principale

app.register_blueprint(education, url_prefix='/webhook')
app.register_blueprint(wealther, url_prefix='/webhook')

if __name__ == "__main__":
    app.run()
