from my_app import db
from datetime import datetime


class News(db.Model):

    __tablename__ = 'news_table'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(800))
    create_date = db.Column(db.DateTime, defaulte=datetime.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, description, create_date, author):
        self.title = title
        self.description = description
        self.create_date = create_date
        self.author = author


class User(db.Model):

    __tablename__='user_table'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    password = db.Column(db.String(15))
    email = db.Column(db.String(50))
    news = db.relationship('News', backref='author') 

    def __init__(self, name, age, password, email,):
        self.name = name
        self.age = age
        self.password = password
        self.email = email


class Flower(db.Model):

    __tablename__ = 'flower_table'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    flower_name = db.Column(db.String(50))
    flower_description = db.Column(db.String(500))
    flower_image = db.Column(db.String(1000))

    def __init__(self, flower_name, flower_description, flower_image):
        self.flower_name = flower_name
        self.flower_description = flower_description
        self.flower_image = flower_image
