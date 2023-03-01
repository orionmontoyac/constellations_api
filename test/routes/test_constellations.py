import json

import pytest

from app import create_app
from test.routes.data_constellations import GET_CONSTELLATIONS_RESPONSE_OK
from api.schemas.schemas import ConstellationSchema


@pytest.fixture
def client():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    with create_app().test_client() as client:
        yield client


class TestConstellation:
    def test_get_all_constellations_ok(self, client):
        url = "/api/v1/constellations"
        response = client.get(url, data=json.dumps(GET_CONSTELLATIONS_RESPONSE_OK))
        data = response.get_json()

        assert response.status_code == 200
        # Check data response schema
        constellation_schema = ConstellationSchema()
        constellation_schema.load(response.get_json(), many=True)


"""
def test_health(client):
    assert client.get("/health").status_code == 200
"""

