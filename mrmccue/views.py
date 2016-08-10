from mrmccue import app
from flask import render_template
import collections

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/keys/')
def keys():
    dl = collections.namedtuple('Download', ['url', 'name'])
    download_links = [
        dl('https://github.com/bowbahdoe/Keys', 'Keys'),
        dl('https://github.com/bowbahdoe/keys-2', 'Keys-2'),
        dl('https://github.com/bowbahdoe/Keys-3-backend', 'Keys-3-backend'),
        dl('https://github.com/bowbahdoe/Keys-3-frontend', 'Keys-3-frontend'),
        dl('https://github.com/bowbahdoe/Keys-3-C', 'Keys-3-C')
    ]
    context = {'download_links': download_links}
    return render_template('projects/keys.html', **context)

@app.errorhandler(404)
def page_not_found(*args, **kwargs):
    return render_template('404.html')
