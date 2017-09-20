# Deps base
FROM alpine:3.6 as base
RUN apk --no-cache add python2 uwsgi uwsgi-python curl py2-pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Pylint stage
FROM base as pylint
COPY requirements-pylint.txt requirements-pylint.txt
RUN pip install -r requirements-pylint.txt
COPY server.py server.py
RUN pylint server.py

# Build stage
FROM base
COPY server.py server.py
EXPOSE 80
HEALTHCHECK CMD ["curl", "-f", "http://localhost/healthz"]
CMD ["uwsgi", "--http-socket", "0.0.0.0:80", "--plugin", "python", \
     "--manage-script-name", "--mount", "/=server:app"]
