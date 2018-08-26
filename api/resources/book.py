from flask import jsonify, request
from flask_restful import Resource
from extensions import db
from api.models import Book


class BookResource(Resource):

    def post(self):
        args = request.get_json()
        title = args['title']
        description = args['description']
        author = args['author']
        book = Book(title=title, description=description, author=author)
        book.save()
        return jsonify({'message':'Saved', 'code':'200'})

    def get(self, id_book=None):
        if id_book is None:
            data = Book.query.all()
            return jsonify([book.to_dict() for book in data])
        book = Book.query.filter_by(id=id_book).first()
        return jsonify(book.to_dict())
