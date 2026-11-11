import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_status(client):
    resp = client.get("/")
    assert resp.status_code == 200


def test_index_content(client):
    resp = client.get("/")
    assert b"Version" in resp.data


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"


def test_ready(client):
    resp = client.get("/ready")
    assert resp.status_code == 200
    assert resp.get_json()["ready"] is True


def test_api_info_version(client):
    resp = client.get("/api/info")
    assert resp.status_code == 200
    assert "version" in resp.get_json()


def test_api_info_status(client):
    resp = client.get("/api/info")
    assert resp.get_json()["status"] == "ok"
