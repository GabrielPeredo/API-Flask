from flask import Flask
from flask_cors import CORS
from database import db, ma
from productos.views import productos


def create_app(config_file='settings.py'):
    application = Flask(__name__)
    application.config.from_pyfile(config_file)
    CORS(application)
    db.init_app(application)
    with application.app_context():
        db.create_all()
    ma.init_app(application)
    application.register_blueprint(productos, url_prefix='/producto')
    return application


if __name__ == '__main__':
    app = create_app()
    app.run(debug=False, port=4000)
