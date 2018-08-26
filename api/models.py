from datetime import datetime
from extensions import db


historic = db.Table('Historic', db.Column('id_client',
                                           db.Integer, db.ForeignKey('Client.id'), primary_key=True),
                                           db.Column('id_book', db.Integer, db.ForeignKey('Book.id'), primary_key=True),
                                           db.Column('reading_date', db.DateTime, default=datetime.utcnow))

class Client(db.Model):
    __tablename__ = "Client"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(70), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return "Client <{}>".format(self.username)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }


class Book(db.Model):
    __tablename__ = "Book"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(60), nullable=False)
    description = db.Column(db.Text)
    author = db.Column(db.String(40))

    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "author": self.author
        }

    def __repr__(self):
        return "Book <{}>".format(self.title)
