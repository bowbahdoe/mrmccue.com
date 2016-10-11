from flask import Blueprint, jsonify
from flask_restful import reqparse, abort, Api, Resource
from location_tracker.models import Location


location_tracker = Blueprint('location-tracker')
location_tracker_api = Api(location_tracker)

location_tracker_api.add_resource(Location, '/ethans_location')


