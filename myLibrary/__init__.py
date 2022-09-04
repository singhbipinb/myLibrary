from flask import Flask, make_response
from config import Config
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)


@app.route("/")
def welcome():
    return make_response("Welcome to myLibrary")

from myLibrary.books import books as books
from myLibrary.transactions import transaction
app.register_blueprint(books)
app.register_blueprint(transaction)
