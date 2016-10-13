from flask import Blueprint, jsonify,request
from flask_restful import abort
from location_tracker.models import LocationModel
from datetime import datetime

location_tracker = Blueprint('location_tracker', __name__)


############################
# UNHELPFUL, REPLACE QUICK #
############################
@location_tracker.errorhandler(404)
def page_not_found(e):
    return jsonify({"message":"Incorrect Call to API"})
    
def try_to_convert(data, data_type):
    try:
        return data_type(data)
    except:
        abort(500)
    
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
        abort(404)
        
def get_all_elements(obj):
    return [obj.__getattr__(i) for i in dir(obj)]
        
@location_tracker.route("/ethans_location", 
                        methods= ['PUT', 'POST'])
def store_location():
    '''
    stores a location given as latitude and longitude
    '''
    print(request.form)

    if 'latitude' not in request.form and 'longitude' not in request.form:
        abort(404)
    else:
        latitude = try_to_convert(request.form['latitude'], float)
        longitude = try_to_convert(request.form['longitude'], float)
    print(latitude)
    print(longitude)
    new_object = LocationModel()
    new_object.latitude = latitude
    new_object.longitude = longitude
    new_object.time_visited = datetime.now()
    print(new_object)
    new_object.save()




