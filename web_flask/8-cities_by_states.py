#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

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


@app.route("/states_list", strict_slashes=False)
def citylist():
    """displays html"""
    statesList = storage.all(State).values()
    statesList = sorted(statesList, key=lambda k: k.name)
    stateCities = []
    for st in sts:
        stateCities.append([st, sorted(state.cities, key=lambda k: k.name)])
    return render_template("8-cities_by_states.html",
                            sts=stateCities,
                            hd="States")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
