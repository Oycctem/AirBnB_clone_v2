#!/usr/bin/python3
""" Flask web application """

from flask import Flask, render_template
import models
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Returns HTML page with states listed """
    states = storage.all(models.State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """ closes the storage """
    storage.close()



if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port)
