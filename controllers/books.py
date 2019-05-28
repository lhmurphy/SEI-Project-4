from flask import Blueprint
from pony.orm import db_session
from models.Book import Book, BookSchema

router = Blueprint(__name__, 'books')

@router.route('/books', methods=['GET'])
@db_session
def index():
    schema = BookSchema(many=True)
    books = Book.select()
    return schema.dumps(books)
