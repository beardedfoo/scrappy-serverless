default: docker-compose

docker-compose: build-docker-compose run-docker-compose
build-docker-compose:
	docker-compose build --force-rm
run-docker-compose:
	docker-compose up

dev:
	watchexec --restart make

test:
	curl -v --fail --silent http://localhost:8000/healthz
