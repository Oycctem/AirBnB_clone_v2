#!/usr/bin/python3
""" Flask web application """

from flask import Flask
app = Flask(__name__)

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def index(text="is cool"):
    """ Returns Python followed by the value of text """
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port)
