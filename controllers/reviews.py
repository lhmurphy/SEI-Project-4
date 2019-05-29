from flask import Blueprint, request, jsonify, abort
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.Review import Review, ReviewSchema

router = Blueprint(__name__, 'reviews') # creates a router for this controller

@router.route('/reviews', methods=['GET'])
@db_session # Allows access to the database in the `index` function
def index():
    # This will serialize our data
    # `many=True` because there are many reviews, ie we expect a list
    schema = ReviewSchema(many=True)
    reviews = Review.select() # get all the reviews
    return schema.dumps(reviews) # `schema.dumps` converts the list to JSON


@router.route('/reviews', methods=['POST'])
@db_session
def create():
    # This will deserialize the JSON from insomnia
    schema = ReviewSchema()

    try:
        # attempt to convert the JSON into a dict
        data = schema.load(request.get_json())
        # Use that to create a review object
        review = Review(**data)
        # store it in the database
        db.commit()
    except ValidationError as err:
        # if the validation fails, send back a 422 response
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    # otherwise, send back the review data as JSON
    return schema.dumps(review), 201


@router.route('/reviews/<int:review_id>', methods=['GET'])
@db_session
def show(review_id):
    # This will serialize our data
    schema = ReviewSchema()
    # This gets a review by ID
    review = Review.get(id=review_id)

    # If we can't find a review, send a 404 response
    if not review:
        abort(404)

    # otherwise, send back the review data as JSON
    return schema.dumps(review)


@router.route('/reviews/<int:review_id>', methods=['PUT'])
@db_session
def update(review_id):
    schema = ReviewSchema()
    review = Review.get(id=review_id)

    if not review:
        abort(404)

    try:
        data = schema.load(request.get_json())
        review.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return schema.dumps(review)


@router.route('/reviews/<int:review_id>', methods=['DELETE'])
@db_session
def delete(review_id):
    review = Review.get(id=review_id)

    if not review:
        abort(404)

    review.delete()
    db.commit()

    return '', 204
