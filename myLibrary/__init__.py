from flask import Flask
from config import Config
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)

from myLibrary.books import books as books
from myLibrary.transactions import transaction
app.register_blueprint(books)
app.register_blueprint(transaction)
