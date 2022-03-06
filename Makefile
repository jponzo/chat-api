export ROOT_DIR=${PWD}

run:
	docker-compose up
build:
	docker-compose build
test:
	docker-compose run api pytest --capture=no  --cov-report html --cov
test-debug:
	docker-compose run api pytest --capture=no  --cov-report html --cov --pdb
stop:
	docker-compose down
