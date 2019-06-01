from datetime import datetime
from pony.orm import Required, Set, Optional
from app import db
from marshmallow import Schema, fields, post_load

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
    user = fields.Nested('UserSchema', exclude=('books', ))
    # likes =
    # user
    # rating


class Book(db.Entity):
    title = Required(str, unique=True)
    author = Required(str)
    isbn = Required(str, unique=True)
    genre = Required(str)
    date = Required(int)
    jacket = Required(str, unique=True)
    description = Required(str)
    fiction = Optional(bool)
    locations = Set('Location')
    reviews = Set('Review')

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    isbn = fields.Str(required=True)
    genre = fields.Str(required=True)
    date = fields.Int(required=True)
    jacket = fields.Str(required=True)
    description = fields.Str(required=True)
    fiction = fields.Bool(required=True)
    locations = fields.Nested('LocationSchema', many=True, exclude=('books', ))
    reviews = fields.Nested('ReviewSchema', many=True)

    @post_load
    def load_bread(self, data):
        data['review'] = Review.get(id=data['review'])
        del data['review_id']

        return data

    @post_load
    def load_locations(self, data):
        data['locations'] = [Location.get(id=location_id) for location_id in data['location_ids']]
        del data['location_ids']

        return data
