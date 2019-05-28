from flask import Blueprint, request, jsonify, abort
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.Location import Location, LocationSchema

router = Blueprint(__name__, 'locations') # creates a router for this controller

@router.route('/locations', methods=['GET'])
@db_session # Allows access to the database in the `index` function
def index():
    # This will serialize our data
    # `many=True` because there are many locations, ie we expect a list
    schema = LocationSchema(many=True)
    locations = Location.select() # get all the locations
    return schema.dumps(locations) # `schema.dumps` converts the list to JSON


@router.route('/locations', methods=['POST'])
@db_session
def create():
    # This will deserialize the JSON from insomnia
    schema = LocationSchema()

    try:
        # attempt to convert the JSON into a dict
        data = schema.load(request.get_json())
        # Use that to create a location object
        location = Location(**data)
        # store it in the database
        db.commit()
    except ValidationError as err:
        # if the validation fails, send back a 422 response
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    # otherwise, send back the location data as JSON
    return schema.dumps(location), 201


@router.route('/locations/<int:location_id>', methods=['GET'])
@db_session
def show(location_id):
    # This will serialize our data
    schema = LocationSchema()
    # This gets a location by ID
    location = Location.get(id=location_id)

    # If we can't find a location, send a 404 response
    if not location:
        abort(404)

    # otherwise, send back the location data as JSON
    return schema.dumps(location)


@router.route('/locations/<int:location_id>', methods=['PUT'])
@db_session
def update(location_id):
    schema = LocationSchema()
    location = Location.get(id=location_id)

    if not location:
        abort(404)

    try:
        data = schema.load(request.get_json())
        location.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return schema.dumps(location)


@router.route('/locations/<int:location_id>', methods=['DELETE'])
@db_session
def delete(location_id):
    location = Location.get(id=location_id)

    if not location:
        abort(404)

    location.delete()
    db.commit()

    return '', 204
