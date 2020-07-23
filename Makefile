DOCKER_COMPOSE=docker-compose

help:
	@echo "commands:"
	@echo
	@echo "make build: docker-compose build"
	@echo "make up:    docker-compose up"
	@echo "make test:  docker-compose run --service-ports app ./scripts/test.sh"
	@echo "make run:   docker-compose run --service-ports app bash"
	@echo "make stop:  docker-compose stop"

build:
	$(DOCKER_COMPOSE) build

up:
	$(DOCKER_COMPOSE) up

test:
	$(DOCKER_COMPOSE) run --service-ports app ./scripts/test.sh

run:
	$(DOCKER_COMPOSE) run --service-ports app bash

debug:
	$(DOCKER_COMPOSE) run --service-ports app ./docker/django/start-server.sh

lint:
	$(DOCKER_COMPOSE) run app flake8

stop:
	$(DOCKER_COMPOSE) stop

migrate:
	$(DOCKER_COMPOSE) run app ./docker/django/setup-server.sh
