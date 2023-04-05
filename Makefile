dev:
	FLASK_APP=api/api.py FLASK_DEBUG=True flask run
tests:
	pytest -vv
start_database:
	docker-compose -f  api_database/docker-compose.yaml up -d
prepare_database:
	FLASK_APP=api/api.py flask db stamp head
	FLASK_APP=api/api.py flask db migrate
upgrade_database:
	FLASK_APP=api/api.py flask db upgrade
