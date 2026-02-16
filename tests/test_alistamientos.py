import pytest
from app.main import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_get_alistamientos_empty(client):
    response = client.get("/alistamientos")
    assert response.status_code == 200
    assert response.get_json() == []


def test_create_alistamiento_success(client):
    payload = {
        "placa": "XYZ999",
        "mecanico": "Pedro",
        "fecha": "2026-02-16",
        "frenos_ok": True,
        "luces_ok": True,
        "aceite_ok": True,
        "llantas_ok": True,
        "observaciones": "Todo en buen estado"
    }

    response = client.post("/alistamientos", json=payload)

    assert response.status_code == 201
    data = response.get_json()
    assert data["placa"] == "XYZ999"


def test_create_alistamiento_missing_fields(client):
    payload = {
        "placa": "AAA111"
    }

    response = client.post("/alistamientos", json=payload)

    assert response.status_code == 400


def test_delete_alistamiento_success(client):
    payload = {
        "placa": "DEL123",
        "mecanico": "Ana",
        "fecha": "2026-02-16",
        "frenos_ok": True,
        "luces_ok": True,
        "aceite_ok": True,
        "llantas_ok": True,
        "observaciones": "OK"
    }

    client.post("/alistamientos", json=payload)

    response = client.delete("/alistamientos/DEL123")

    assert response.status_code == 204

def test_delete_alistamiento_not_found(client):
    response = client.delete("/alistamientos/NOEXISTE")
    assert response.status_code == 404



