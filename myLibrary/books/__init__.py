from flask import Blueprint
books = Blueprint("books", __name__, url_prefix="/api/book")

from myLibrary.books import booksControllers