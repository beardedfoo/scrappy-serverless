# Deps base
FROM alpine as base
RUN apk --no-cache add python2 uwsgi uwsgi-python py2-flask curl py2-pip
RUN pip install docker==2.4.2

# Pylint stage
FROM base as pylint
RUN pip install pylint
COPY server.py server.py
RUN pylint server.py
COPY shim.py shim.py
RUN pylint shim.py

# Build stage
FROM base
COPY server.py server.py
EXPOSE 80
HEALTHCHECK CMD ["curl", "-f", "http://localhost/healthz"]
CMD ["uwsgi", "--http-socket", "0.0.0.0:80", "--plugin", "python", \
     "--manage-script-name", "--python-autoreload", "1", \
     "--enable-threads", "--threads", "10", "--mount", "/=server:app"]
