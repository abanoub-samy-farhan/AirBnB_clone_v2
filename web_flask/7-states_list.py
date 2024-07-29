#!/usr/bin/python3
"""Doc Model"""
from flask import Flask, render_template
from models import *
from models import storage
from models.state import State


"""Making the App"""
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def getting_states():
    all_states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    """Making a list of the states found in the file.json"""
    return render_template('7-states_list.html', states=all_states)

@app.teardown_appcontext
def closing(exception):
    """Tearing down app context with closing function for the storage sessions"""
    storage.close()

if __name__ =='__main__':
    app.run(port='5000', host='0.0.0.0')