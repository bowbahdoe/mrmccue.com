import datetime
from mrmccue import db

class LocationModel(db.Document):
    latitude  = db.FloatField()
    longitude = db.FloatField()
    time_visited = db.DateTimeField()