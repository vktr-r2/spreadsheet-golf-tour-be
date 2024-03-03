from flask import Flask, Blueprint
from flask_restful import Api
import logging
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

api_blueprint = Blueprint("api", __name__)

app.logger.setLevel(logging.DEBUG)

# Load and store env variables from .env file
load_dotenv()
database_url = os.environ.get("DATABASE_URL")


# Config database
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

api = Api(api_blueprint)


def make_api():
    from spreadsheet_golf_tour_be.resources.home import HomeResource
    from spreadsheet_golf_tour_be.resources.login import LoginResource

    # Home
    api.add_resource(HomeResource, "/")

    # Login
    api.add_resource(LoginResource, "/login")

    return api


make_api()

app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
