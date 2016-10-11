import datetime
from mrmccue import db
from flask_restful import Resource

class LocationModel(db.Document):
    latitude  = db.FloatField()
    longitude = db.FloatField()
    time_visited = db.DateTimeField()

class Location(LocationModel, Resource):
    def get(self):
        '''
        Fetches the most Recent Location
        '''
        most_recent_location = self.objects.order_by('-id').first()
        return {
            "latitude" : most_recent_location.latitude,
            "longitude": most_recent_location.longitude,
            "time_visited": most_recent_location.time_visited
        }

    def put(self, latitude: float, longitude: float):
        '''
        stores a location given as latitude and longitude
        '''
        new_object = self()
        new_object.latitude = latitude
        new_object.longitude = longitude
        new_object.time_visited = datetime.now()
