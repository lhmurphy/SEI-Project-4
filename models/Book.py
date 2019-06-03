from datetime import datetime
from pony.orm import Required, Set, Optional
from app import db
from marshmallow import Schema, fields, post_load, validates_schema, ValidationError

from .Location import Location

class Review(db.Entity):
    content = Required(str)
    book = Required('Book')
    created_at = Required(datetime, default=datetime.utcnow)
    user = Required('User')

class ReviewSchema(Schema):
    id = fields.Int(dump_only=True)
    content = fields.Str(required=True)
    book = fields.Nested('BookSchema', exclude=('reviews', ))
    created_at = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    user = fields.Nested('UserSchema', exclude=('books', 'reviews'))
    # likes =
    # user
    # rating


class Book(db.Entity):
    title = Required(str)
    author = Required(str)
    isbn = Required(str)
    genre = Required(str)
    date = Optional(int)
    jacket = Required(str)
    description = Required(str)
    fiction = Optional(bool)
    locations = Set('Location')
    reviews = Set('Review')
    user = Required('User')

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    isbn = fields.Str(required=True)
    genre = fields.Str(required=True)
    date = fields.Int(required=False)
    jacket = fields.Str(required=True)
    description = fields.Str(required=True)
    fiction = fields.Bool(required=False)
    locations = fields.Nested('LocationSchema', many=True, exclude=('books', ), dump_only=True)
    location_ids = fields.List(fields.Int(), load_only=True)
    reviews = fields.Nested('ReviewSchema', many=True, dump_only=True, exclude=('book', ))
    user = fields.Nested('UserSchema', exclude=('books', 'reviews'))

    @post_load
    def load_locations(self, data):
        data['locations'] = [Location.get(id=location_id) for location_id in data['location_ids']]
        del data['location_ids']

        return data
