"""
This script runs the TestFlaskJadeWeb application using a development server.
"""

from os import environ
from TestFlaskJadeWeb import app
from flask import url_for

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    app.secret_key = 'capstone_secret_key'

    app.run(HOST, PORT)