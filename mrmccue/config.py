# REMEMBER TO CHANGE THE DEBUG FLAG
# DURING PRODUCTION
DEBUG = True

# Used for WTForms
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# and mongoengine
MONGODB_SETTINGS = {
    'db': 'mrmccue',
    'host': 'ds059306.mlab.com',
    'port': 59306,
    'username': 'bowbahdoe',
    'password': 'pie1222'
}

# Flask-Security config
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE  = True
SECURITY_CHANGEABLE   = True
SECURITY_URL_PREFIX   = '/security'