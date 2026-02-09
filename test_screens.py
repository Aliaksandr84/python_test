"""
Basic tests for new Flask screens.
"""
import pytest
from app import app as flask_app

@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client

def test_dashboard(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Dashboard" in resp.data

def test_upload_get(client):
    resp = client.get("/upload")
    assert resp.status_code == 200
    assert b"Upload" in resp.data

def test_reports(client):
    resp = client.get("/reports")
    assert resp.status_code == 200
    assert b"Reports" in resp.data