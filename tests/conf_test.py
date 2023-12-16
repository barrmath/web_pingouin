import pytest

from pingouin_app.views import create_app


# on crée un client pour les tests

@pytest.fixture
def client():
    app = create_app()
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client
