import json
from app.main import create_app

def test_get_citas_vacio():
    app = create_app()
    client = app.test_client()

    response = client.get("/citas")

    assert response.status_code == 200
    assert response.json == []

def test_post_citas_crea_cita():
    app = create_app()
    client = app.test_client()

    nueva_cita = {
        "cliente": "Test Cliente",
        "fecha": "2026-02-11",
        "hora": "09:00"
    }

    response = client.post(
        "/citas",
        data=json.dumps(nueva_cita),
        content_type="application/json"
    )

    assert response.status_code == 201
    assert response.json["cliente"] == "Test Cliente"
