from app import db
from pony.orm import Required, Set
from marshmallow import Schema, fields

class Location(db.Entity):
    name = Required(str)
    books = Set('Book')

class LocationSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    books = fields.Nested('BookSchema', many=True, exclude=('locations', ))
