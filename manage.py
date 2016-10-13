#!/usr/bin/python3
from flask_script import Manager
from flask import url_for
from mrmccue import app

manager = Manager(app)


@manager.command
def list_routes():
    '''
    Helper to list routes (like Rail's rake routes)
    
    Posted by Jonathan Tushman on 2013-10-03 
    http://flask.pocoo.org/snippets/117/
    '''
    output = []
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        line = url_for(rule.endpoint, **options)
        output.append(line)
    
    for line in sorted(output):
        print(line)

if __name__ == "__main__":
    #manager.run()
    app.run(port=8080,
            host='0.0.0.0')
