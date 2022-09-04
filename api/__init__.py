from flask import Flask, make_response
from config import Config
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)


@app.route("/")
def welcome():
    return make_response("Welcome to myLibrary")

from api.books import books as books
from api.transactions import transaction
app.register_blueprint(books)
app.register_blueprint(transaction)
