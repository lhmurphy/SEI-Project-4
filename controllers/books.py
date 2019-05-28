from flask import Blueprint, request, jsonify, abort
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

@router.route('/books/<int:book_id>', methods=['GET'])
@db_session
def show(book_id):
    schema = BookSchema()
    book = Book.get(id=book_id)

    if not book:
        abort(404)

    return schema.dumps(book)

@router.route('/books/<int:book_id>', methods=['PUT'])
@db_session
def update(book_id):
    schema = BookSchema()
    book = Book.get(id=book_id)

    if not book:
        abort(404)

    try:
        data = schema.load(request.get_json())
        book.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return schema.dumps(book)
