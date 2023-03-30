import pytest

from api.api import create_app


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


class TestHealth:
    def setup_method(self):
        self.health_check_url = "/api/v1/health"

    def test_get_health_check_ok(self, client):
        response = client.get(self.health_check_url)

        assert response.status_code == 200
