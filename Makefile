.PHONY: build run test

all: build run

build:
	docker-compose build salary_watcher

run:
	docker-compose up salary_watcher

test:
	pytest test_main.py