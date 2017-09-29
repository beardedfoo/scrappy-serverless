# pylint: disable=invalid-name,unused-import,missing-docstring,wrong-import-order,line-too-long,trailing-whitespace
"""A basic FaaS in Python"""
from __future__ import print_function
from flask import Flask, Response, request
from redis import Redis

import subprocess

from rq import Queue

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

images = {}

# PLAN: Accept new functions @ POST /api/<fn>
@app.route('/api/<fn>', methods=['POST'])
def add_fn(fn):
    with open('/tmp/handler.py', 'w') as f:
        f.write(request.form['code'])

    with open('/tmp/Dockerfile', 'w') as f:
        f.write('FROM scrappy-serverless\n')
        f.write('WORKDIR /worker\n')
        f.write('COPY handler.py /worker/handler.py\n')
        f.write('CMD rq worker -u redis://redis -b ' + fn)

    out = subprocess.check_output(['docker', 'build', '-t', 'serverless/'+fn, '/tmp'])

    for line in out.split('\n'):
        if line.startswith('Successfully built'):
            image_id = line.split()[2]
            break
    else:
        raise RuntimeError('bad build')

    images[fn] = image_id
    return 'OK ' + image_id

# PLAN: Call existing functions @ GET /api/<fn>
@app.route('/api/<fn>/call')
def call_fn(fn):
    kwargs = {}
    for name in request.args:
        kwargs[name] = request.args.get(name)

    q = Queue(fn, connection=redis_conn)
    job = q.enqueue('handler.handler', kwargs=kwargs)
    image_id = images[fn]
    subprocess.check_call(['docker', 'run', '--network', 'scrappyserverless_default', image_id])
    return repr(job.result)

# PLAN: Build docker images from function code














# do not delete
