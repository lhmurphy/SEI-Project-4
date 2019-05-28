from flask import Blueprint, request, jsonify
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.Book import Book, BookSchema

router = Blueprint(__name__, 'books')

@router.route('/books', methods=['GET'])
@db_session
def index():
    schema = BookSchema(many=True)
    books = Book.select()
    return schema.dumps(books)

@router.route('/books', methods=['POST'])
@db_session
def create():
    schema = BookSchema()

    try:
        data = schema.load(request.get_json())
        book = Book(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validarion failed', 'errors': err.message}), 422

    return schema.dumps(book), 201
