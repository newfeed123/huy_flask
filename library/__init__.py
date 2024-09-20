from flask import Flask, request, Blueprint
from .books.controller import books
from .extension import db
import os
from .model import Student, Books, Author, Category, Borrow

def create_db(app):
    if os.path.exists("library/library.db"):
        db.create_all(app = app)
        print("create db !!!!")

def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
    db.init_app(app)
    app.config.from_pyfile(config_file)
    app.register_blueprint(books)
    create_db(app)
    print(app.config["SECRET_KEY"])
    return app

