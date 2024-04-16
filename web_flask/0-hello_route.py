#!/usr/bin/python3
""" Flask web application """

from flask import Flask
app = Flask(__name__)


@app.route('/airbnb-onepag', strict_slashes=False)
def index():
    """ Returns hello HBNB! """
    return 'Hello HBNB!'

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port)
