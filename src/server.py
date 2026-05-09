from flasgger import Swagger
from flask import Flask, Blueprint

from src import config
from src.models import db

server = Flask(__name__)

# ---------------- Swagger config ----------------
server.config["SWAGGER"] = {
    "swagger_version": "2.0",
    "title": "Application",
    "specs": [
        {
            "version": "0.0.1",
            "title": "Application",
            "endpoint": "spec",
            "route": "/application/spec",
            "rule_filter": lambda rule: True,
        }
    ],
    "static_url_path": "/apidocs",
}

Swagger(server)

# ---------------- DB config ----------------
server.debug = config.DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(server)

# ---------------- IMPORT ROUTES (IMPORTANT: après création app) ----------------
from src import routes

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(blueprint, url_prefix=config.APPLICATION_ROOT)

# ---------------- RUN ----------------
if __name__ == "__main__":
    server.run(host=config.HOST, port=config.PORT)
