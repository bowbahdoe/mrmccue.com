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

class Location(Resource):
    def get(self):
        '''
        Fetches the most Recent Location
        '''
        most_recent_location = LocationModel.objects.order_by('-id').first()
        return {
            "latitude" : most_recent_location.latitude,
            "longitude": most_recent_location.longitude,
            "time_visited": most_recent_location.time_visited
        }

    def put(self, latitude: float, longitude: float):
        '''
        stores a location given as latitude and longitude
        '''
        new_object = LocationModel()
        new_object.latitude = latitude
        new_object.longitude = longitude
        new_object.time_visited = datetime.now()
        new_object.save()

#######################################
# implicitly adds it to the blueprint #
#######################################
_API.add_resource(Location,'/ethans_location/<float:latitude><float:longitude>')


