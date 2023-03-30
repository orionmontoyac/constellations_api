dev:
	FLASK_APP=./api/api.py FLASK_DEBUG=True flask run
start_database:
	docker-compose -f  api_database/docker-compose.yaml up -d