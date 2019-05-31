from flask import Blueprint, request, jsonify, abort, g
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.Book import Book, BookSchema, Review, ReviewSchema
from lib.secure_route import secure_route

router = Blueprint(__name__, 'books')

@router.route('/books', methods=['GET'])
@db_session
def index():
    schema = BookSchema(many=True)
    books = Book.select()
    return schema.dumps(books)

@router.route('/books', methods=['POST'])
@db_session
@secure_route
def create():
    schema = BookSchema()

    try:
        data = schema.load(request.get_json())
        book = Book(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.message}), 422

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
@secure_route
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

@router.route('/books/<int:book_id>', methods=['DELETE'])
@db_session
@secure_route
def delete(book_id):
    book = Book.get(id=book_id)

    if not book:
        abort(404)

    book.delete()
    db.commit()

    return '', 204

@router.route('/books/<int:book_id>/books', methods=['POST'])
@secure_route
@db_session
def create_review(book_id):
    book_schema = BookSchema()
    review_schema = ReviewSchema()
    book = Book.get(id=book_id)

    try:
        data = review_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    Review(**data, book=book, user=g.current_user)
    db.commit()

    return book_schema.dumps(book)


@router.route('/books/<int:book_id>/books/<int:review_id>', methods=['DELETE'])
@secure_route
@db_session
def delete_review(book_id, review_id):

    schema = BookSchema()
    book = Book.get(id=book_id)
    review = Review.get(id=review_id)
    review.delete()
    db.commit()


    return schema.dumps(book)
