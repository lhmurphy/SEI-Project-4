from pony.orm import Required, Optional
from app import db
from marshmallow import Schema, fields

class Book(db.Entity):
    title = Required(str, unique=True)
    author = Required(str)
    isbn = Required(int)
    genre = Required(str)
    pub_date = Required(int)
    book_jacket = Required(str, unique=True)
    description = Required(str)
    fiction = Required(bool)
    location = Required(str)
    comment = Optional(str)

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    isbn = fields.Int(required=True)
    genre = fields.Str(required=True)
    pub_date = fields.Int(required=True)
    book_jacket = fields.Str(required=True)
    description = fields.Str(required=True)
    fiction = fields.Bool(required=True)
    location = fields.Str(required=True)
    comment = fields.Str(required=False)
