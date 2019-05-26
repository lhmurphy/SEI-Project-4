from flask import Flask
from pony.orm import Database, db_session

app = Flask(__name__)
db = Database()
db.bind(provider='postgres', dbname='travel-books')
from models.Book import Book, BookSchema

db.generate_mapping(create_tables=True)

@app.route('/books', methods=['GET', 'POST'])
@db_session
def index():
    books_schema = BookSchema(many=True)
    books = Book.select()
    return books_schema.dumps(books)
