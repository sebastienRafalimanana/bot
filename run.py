import app as boot
from config import Config

app = boot.create_app()

if __name__ == "__main__":
    app.run(Config.APP_HOST,Config.APP_PORT)