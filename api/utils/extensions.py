from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flasgger import Swagger

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
swagger = Swagger()
