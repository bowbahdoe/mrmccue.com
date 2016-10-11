from flask import Blueprint, jsonify
from flask_restful import reqparse, abort, Api, Resource
from location_tracker.models import Location


location_tracker = Blueprint('location-tracker')

######################################################################
# We initialize the Api object using the private convention because  #
# we should only ever reference the Blueprint object outside of this #
# module, and not the Api directly                                   #
######################################################################
_API = Api(location_tracker)

_API.add_resource(Location,'/ethans_location/<float:latitude><float:longitude>')


