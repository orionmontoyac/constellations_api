from flask import Flask
from flask_migrate import Migrate

from api.utils.database import db
from api.routes.constellations import constellations_v1_bp
from api.routes.stars import stars_v1_bp


def create_app() -> Flask:
    new_app = Flask(__name__)
    new_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///constellations.sqlite3'
    new_app.config['SWAGGER'] = {
        'title': 'Flask API Starter Kit',
    }
    # config data base
    db.init_app(new_app)
    Migrate(new_app, db, render_as_batch=True)

    # Initialize Config
    new_app.config.from_pyfile('config.py')

    # Blue prints
    new_app.register_blueprint(constellations_v1_bp)
    new_app.register_blueprint(stars_v1_bp)

    return new_app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)