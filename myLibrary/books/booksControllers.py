from flask import make_response, request, jsonify
import json
from myLibrary.books import books
from bson.json_util import dumps
from myLibrary import mongo


# Search by book name/term
@books.route("/search/byname/<string:name>", methods=["GET"])
def search_book(name):
    regex = "^" + name
    booklist = mongo.db.books.find({"name": {"$regex": regex, '$options': 'i'}})
    books = dumps(booklist)

    if len(books) > 0:
        response = make_response(jsonify({"Books": json.loads(books)}), 200)
        return response
    else:
        response = make_response(jsonify({"message": "No Books Found"}), 200)
        return response

    return make_response(jsonify({"message": "Something went wrong"}), 401)


# Search by rent range
@books.route("/search/byrent", methods=["GET"])
def search_rent():
    min = int(request.args["min"])
    max = int(request.args["max"])
    booklist = mongo.db.books.find({"rent_per_day": {"$gte": min, "$lte": max}})

    books = dumps(booklist)

    if len(books) > 0:
        response = make_response(jsonify({"Books": json.loads(books)}), 200)
        return response
    else:
        response = make_response(jsonify({"message": "No Books Found"}), 200)
        return response

    return make_response(jsonify({"message": "Something went wrong"}), 401)


# Search by category, name and rent range
@books.route("/search/<category>/<term>", methods=["GET"])
def search_category(category, term):
    regex = "^" + term
    min = int(request.args["min"])
    max = int(request.args["max"])
    booklist = mongo.db.books.find({"$and": [{"category": category}, {"name": {"$regex": regex, '$options': 'i'}},
                                             {"rent_per_day": {"$gte": min, "$lte": max}}]})

    books = dumps(booklist)

    if len(books) > 0:
        response = make_response(jsonify({"Books": json.loads(books)}), 200)
        return response
    else:
        response = make_response(jsonify({"message": "No Books Found"}), 200)
        return response

    return make_response(jsonify({"message": "Something went wrong"}), 401)
