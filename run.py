from flask import Flask
import os 
import config
from models import db
def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config.from_object(config.DevelopmentConfig)
    db.init_app(app)
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    return app
if __name__ == "__main__":
    app = create_app()
    app.run()