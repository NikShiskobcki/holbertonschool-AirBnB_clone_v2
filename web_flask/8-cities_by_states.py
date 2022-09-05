#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from os import environ

app = Flask(__name__)


@app.teardown_appcontext
def teadown(self):
    """handle teardown"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def stateslist():
    """displays html"""
    statesList = storage.all(State).values()
    statesList = sorted(statesList, key=lambda k: k.name)
    return render_template("7-states_list.html", statesList=statesList)

@app.route("/cities_by_states", strict_slashes=False)
def citiesState():
    """displays html"""
    statesList = storage.all(State).values()
    statesList = sorted(statesList, key=lambda k: k.name)
    return render_template("8-cities_by_states.html", statesList=statesList)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
