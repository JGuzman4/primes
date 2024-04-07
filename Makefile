.PHONY: build run

build:
	docker build -t bizarre-ride .

run: build
	docker run -v $$PWD:/app bizarre-ride
