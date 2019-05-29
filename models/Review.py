from datetime import datetime
from app import db
from pony.orm import Required
from marshmallow import Schema, fields

class Review(db.Entity):
    title = Required(str)
    content = Required(str)
    book = Required('Book')
    created_at = Required(datetime, default=datetime.utcnow)

class ReviewSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    book = fields.Nested('BookSchema', exclude=('reviews', ))
    created_at = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    # likes =
    # user
    # rating
