from flask import Blueprint, jsonify,request
from flask_restful import abort
from location_tracker.models import LocationModel
from location_tracker.helpers import try_to_convert
from datetime import datetime


location_tracker = Blueprint('location_tracker', __name__)

@location_tracker.route("/ethans_location", methods= ['GET'])
def get_location():
    '''
    Fetches the most Recent Location
    '''
    most_recent_location = LocationModel.objects
    print(most_recent_location)
    if most_recent_location:
        return  jsonify({
                    "latitude" : most_recent_location.latitude,
                    "longitude": most_recent_location.longitude,
                    "time_visited": most_recent_location.time_visited
                    })
    else:
        abort(400)
        
@location_tracker.route("/ethans_location", 
                        methods= ['PUT', 'POST'])
def store_location():
    '''
    stores a location given as latitude and longitude
    '''

    if 'latitude' not in request.form and 'longitude' not in request.form:
        abort(404)
    latitude = try_to_convert(request.form['latitude'], float)
    longitude = try_to_convert(request.form['longitude'], float)
    

    new_object = LocationModel(latitude=latitude,
                               longitude=longitude)
    new_object.latitude = latitude
    new_object.longitude = longitude
    new_object.time_visited = datetime.now()
    new_object.save()
    return jsonify({'latitude': latitude,
                    'longitude': longitude}), 200




