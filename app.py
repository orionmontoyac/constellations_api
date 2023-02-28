from flask import Flask
from api.routes.home import home_api
from api.routes.constellations import constellations_v1_bp


def create_app() -> Flask:
    new_app = Flask(__name__)

    new_app.config['SWAGGER'] = {
        'title': 'Flask API Starter Kit',
    }

    # Initialize Config
    new_app.config.from_pyfile('config.py')
    new_app.register_blueprint(home_api, url_prefix='/api')
    new_app.register_blueprint(constellations_v1_bp)

    return new_app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)
