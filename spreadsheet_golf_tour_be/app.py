from flask import Flask
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy

# Create Flask app instance
app = Flask(__name__)

# Load and store env variables from .env file
load_dotenv()
database_url = os.environ.get('DATABASE_URL')


# Config database
app.config["SQLALCHEMY_DATABASE_URI"] = app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route("/")
def hello_world():
    return "Hello, Spreadsheet Golf Tour!"
