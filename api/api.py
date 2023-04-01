from flask import Flask
from flask_migrate import Migrate
from flasgger import Swagger

import config
from api import db
from api.routes.home import home_v1_bp
from api.routes.health_check import health_v1_bp
from api.routes.constellations import constellations_v1_bp
from api.routes.stars import stars_v1_bp
from api.utils.error_handling import errors_v1_bp

# TODO: Add logs
# TODO: Add api key
# TODO: Add more unit test
# TODO: Add home page
# TODO: Add config file
# TODO: Integrate third party API
# TODO: Add Swagger docs


def create_app() -> Flask:
    new_app = Flask(__name__)
    # Initialize Config
    new_app.config.from_object(config.DevelopmentConfig)

    # swagger docs
    swagger = Swagger(new_app)
    # config data base
    db.init_app(new_app)
    Migrate(new_app, db, render_as_batch=True)

    # Blue prints
    new_app.register_blueprint(home_v1_bp)
    new_app.register_blueprint(health_v1_bp)
    new_app.register_blueprint(constellations_v1_bp)
    new_app.register_blueprint(stars_v1_bp)

    # Custom error handlers
    new_app.register_blueprint(errors_v1_bp)

    return new_app


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "-p", "--port", default=5000, type=int, help="port to listen on"
    )
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host="0.0.0.0", port=port)