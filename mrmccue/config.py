# REMEMBER TO CHANGE THE DEBUG FLAG
# DURING PRODUCTION
DEBUG = True

# Used for WTForms
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# and mongoengine
MONGODB_SETTINGS = {
    'db': 'mrmccue',
    'host': 'localhost',
    'port': 27017
}