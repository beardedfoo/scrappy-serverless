default: docker-compose

docker-compose: build up

build:
	docker-compose build --force-rm

up:
	docker-compose up

down:
	docker-compose down

shell:
	docker run --rm --net scrappyserverless_default -v /var/run/docker.sock:/var/run/docker.sock -it scrappy-serverless /bin/sh

dev:
	watchexec --restart make

test:
	curl -v --fail --silent http://localhost:8000/healthz
