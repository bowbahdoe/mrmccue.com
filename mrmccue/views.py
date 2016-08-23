from mrmccue import app
from mrmccue.forms.login import LoginForm, RegistrationForm
from mrmccue.models.user import User
from mrmccue import auth, helpers
from flask import render_template, redirect
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        new_user = User('de@ffr.com', form.username.data, form.password.data)
        new_user.save()
        return redirect('/')
    return render_template('login.html',
                           title='Sign In',
                           form=form)
@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        auth.register_user(form.username.data,
                           form.password.data)
        return redirect('/')
    return render_template('register.html',
                           form=form)
@app.errorhandler(404)
def page_not_found(*args, **kwargs):
    return render_template('error.html', **{'type': 404})
