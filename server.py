# pylint: disable=invalid-name,unused-import,missing-docstring,wrong-import-order,line-too-long,trailing-whitespace
"""A basic FaaS in Python"""
from __future__ import print_function
from flask import Flask, Response, request
from redis import Redis

app = Flask(__name__)

# Connect to redis & test connection
redis_conn = Redis('redis')
redis_conn.info()

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
