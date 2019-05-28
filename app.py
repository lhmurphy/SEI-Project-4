from flask import Flask
from pony.orm import Database

app = Flask(__name__)
db = Database()
db.bind(provider='postgres', dbname='travel-books')

from config import routes

db.generate_mapping(create_tables=True)
