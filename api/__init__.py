from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # NOSONAR

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///loto.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return 'grafolo49 - v0.0.1'
