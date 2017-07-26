# pylint: disable=invalid-name
"""A basic HTTP server in Python"""
from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/healthz')
def healthz():
    """Reports service health"""
    return "OK\n"

@app.route('/')
def index():
    """Serves the home page"""
    return Response(
        "Welcome to basic-http-server, you're ready to add some methods!\n" +
        str(request) + "\n", mimetype='text/plain'
    )
