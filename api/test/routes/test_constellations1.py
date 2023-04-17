import pytest
from api.api import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.from_object(TestingConfig)

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_logout_redirect(client, mocker):
    mock = mocker.patch(
        "api.controllers.constellations.get_all"
    )
    mock.return_value = []

    response = client.get('/api/v1/constellations')
    assert response.status_code == 200
