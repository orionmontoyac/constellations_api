export FLASK_APP="entrypoint:app"
export FLASK_ENV="development"
export APP_SETTINGS_MODULE="config.default"

pip install gunicorn

gunicorn --bind 0.0.0.0:$PORT entrypoint:app