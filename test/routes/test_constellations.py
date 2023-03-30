import pytest

import test.routes.data_constellations as data_constellations
from api.api import create_app
from api.schemas.schemas import ConstellationSchema
from api.utils.database import ConstellationModel


@pytest.fixture
def client():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    with create_app().test_client() as client:
        yield client


class TestConstellation:
    def setup_method(self):
        self.constellations_url = "/api/v1/constellations"
        self.constellation_url = "/api/v1/constellation"

    def test_get_all_constellations_ok(self, client, mocker):
        mock = mocker.patch(
            "api.utils.database.ConstellationModel.get_all_constellations"
        )
        mock.return_value = data_constellations.ALL_CONSTELLATIONS_RESPONSE

        response = client.get(self.constellations_url)

        assert response.status_code == 200
        # Check data response schema
        constellation_schema = ConstellationSchema()
        constellation_schema.load(response.get_json(), many=True)

    def test_post_create_constellations_ok(self, client, mocker):
        mocker.patch("api.utils.database.ConstellationModel.save")

        response = client.post(
            self.constellations_url, json=data_constellations.NEW_CONSTELLATION_REQUEST
        )

        assert response.status_code == 201
        assert response.json == "Constellation(s) saved"

    def test_get_constellation_id_ok(self, client, mocker):
        mock = mocker.patch(
            "api.utils.database.ConstellationModel.get_one_constellation"
        )
        mock.return_value = data_constellations.ALL_CONSTELLATIONS_RESPONSE[0]

        response = client.get("{}/{}".format(self.constellation_url, 1))

        assert response.status_code == 200
        # Check data response schema
        constellation_schema = ConstellationSchema()
        constellation_schema.load(response.get_json())

    def test_get_constellation_bad_id(self, client):
        response = client.get(
            "{}/{}".format(self.constellation_url, "bad_id_constellation")
        )

        assert response.status_code == 404
        assert "message" in response.get_json().keys()
        assert "error" in response.get_json().keys()

    def test_get_constellation_id_not_found(self, client, mocker):
        mock = mocker.patch(
            "api.utils.database.ConstellationModel.get_one_constellation"
        )
        mock.return_value = None
        constellation_id = 99
        response = client.get("{}/{}".format(self.constellation_url, constellation_id))

        assert response.status_code == 404
        assert "message" in response.get_json().keys()
        assert "error" in response.get_json().keys()

    def test_put_constellation_id_ok(self, client, mocker):
        mock = mocker.patch(
            "api.utils.database.ConstellationModel.get_one_constellation"
        )
        mock.return_value = ConstellationModel(
            **data_constellations.NEW_CONSTELLATION_REQUEST[0]
        )

        mock = mocker.patch("api.utils.database.ConstellationModel.update")
        mock.return_value = data_constellations.ALL_CONSTELLATIONS_RESPONSE[0]

        response = client.put(
            "{}/{}".format(self.constellation_url, 1),
            json=data_constellations.UPDATE_CONSTELLATION_REQUEST,
        )

        assert response.status_code == 200
        # Check data response schema
        constellation_schema = ConstellationSchema()
        constellation_schema.load(response.get_json())

    def test_put_constellation_id_not_found(self, client, mocker):
        mock = mocker.patch(
            "api.utils.database.ConstellationModel.get_one_constellation"
        )
        mock.return_value = None

        constellation_id = 99

        response = client.put(
            "{}/{}".format(self.constellation_url, constellation_id),
            json=data_constellations.UPDATE_CONSTELLATION_REQUEST,
        )

        assert response.status_code == 404
        assert "message" in response.get_json().keys()
        assert "error" in response.get_json().keys()

    def test_put_constellation_id_bad_input(self, client, mocker):
        mock = mocker.patch(
            "api.utils.database.ConstellationModel.get_one_constellation"
        )
        mock.return_value = ConstellationModel(
            **data_constellations.NEW_CONSTELLATION_REQUEST[0]
        )
        constellation_id = 99

        response = client.put(
            "{}/{}".format(self.constellation_url, constellation_id),
            json=data_constellations.UPDATE_CONSTELLATION_BAD_REQUEST,
        )

        assert response.status_code == 400
        assert "message" in response.get_json().keys()
        assert "error" in response.get_json().keys()

    def test_delete_constellation_id_ok(self, client, mocker):
        mock = mocker.patch(
            "api.utils.database.ConstellationModel.get_one_constellation"
        )
        mock.return_value = ConstellationModel(
            **data_constellations.NEW_CONSTELLATION_REQUEST[0]
        )

        mock = mocker.patch("api.utils.database.ConstellationModel.delete")
        mock.return_value = {}

        response = client.delete("{}/{}".format(self.constellation_url, 1))

        assert response.status_code == 200

    def test_delete_constellation_id_not_found(self, client, mocker):
        mock = mocker.patch(
            "api.utils.database.ConstellationModel.get_one_constellation"
        )
        mock.return_value = None
        constellation_id = 99

        response = client.delete(
            "{}/{}".format(self.constellation_url, constellation_id)
        )

        assert response.status_code == 404
        assert "message" in response.get_json().keys()
        assert "error" in response.get_json().keys()
