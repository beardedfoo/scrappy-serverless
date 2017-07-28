# pylint: disable=invalid-name,unused-import
"""A basic FaaS in Python"""
from flask import Flask, Response, request

app = Flask(__name__)

# PLAN: Connect to docker & test connection (.info)

# PLAN: Connect to redis & test connection (.info)

@app.route('/healthz')
def healthz():
    """Reports service health"""
    return "OK\n"

# PLAN: Show list of runnable functions @ /
@app.route('/')
def index():
    """Serves the home page"""
    return Response(
        "Welcome to basic-http-server, you're ready to add some methods!\n" +
        str(request) + "\n", mimetype='text/plain'
    )

# PLAN: Accept new functions @ POST /api/<fn>

# PLAN: Call existing functions @ GET /api/<fn>

# PLAN: Build docker images from function code
