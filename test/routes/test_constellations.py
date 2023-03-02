import json

import pytest

from app import create_app
from api.schemas.schemas import ConstellationSchema
from test.routes.data_constellations import ALL_CONSTELLATIONS_RESPONSE, NEW_CONSTELLATION_REQUEST


@pytest.fixture
def client():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    with create_app().test_client() as client:
        yield client


class TestConstellation:

    def setup_method(self):
        self.url = "/api/v1/constellations"

    def test_get_all_constellations_ok(self, client, mocker):
        mock = mocker.patch('api.utils.database.ConstellationModel.get_all_constellations')
        mock.return_value = ALL_CONSTELLATIONS_RESPONSE

        response = client.get(self.url)

        assert response.status_code == 200
        # Check data response schema
        constellation_schema = ConstellationSchema()
        constellation_schema.load(response.get_json(), many=True)

    def test_post_create_constellation_ok(self, client, mocker):
        mocker.patch('api.utils.database.ConstellationModel.save')

        response = client.post(self.url, json=NEW_CONSTELLATION_REQUEST)

        assert response.status_code == 201
        assert response.json == "Constellation(s) saved"
