from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)

# SQLALCHEMY_TRACK_MODIFICATIONS = False
PG_USER = "daria"
PG_PASSWORD = "1"
PG_HOST = "localhost"
PG_PORT = 5432
DB_NAME = "cursor_flask_lesson"
SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"


db = SQLAlchemy(app)

class Flower(db.Model):

    _tablename__ = 'flower_table'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    flower_name = db.Column(db.String(50))
    flower_description = db.Column(db.String(500))
    flower_image = db.Column(db.String(1000))

    def __init__(self, flower_name, flower_description, flower_image):
        self.flower_name = flower_name
        self.flower_description = flower_description
        self.flower_image = flower_image