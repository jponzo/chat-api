export ROOT_DIR=${PWD}

run:
	docker-compose up
build:
	docker-compose build
test:
	docker-compose run api pytest --capture=no  --cov-report html --cov
stop:
	docker-compose down
