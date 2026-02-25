import pytest
from app.main import create_app


# --- CONFIGURACIÓN DE PRUEBAS (FIXTURE) ---
# Esto es muy útil: @pytest.fixture define una función que se ejecuta antes de cada test.
# En lugar de repetir "app = create_app()" en cada función, lo hago aquí una sola vez.
@pytest.fixture
def client():
    # 1. Creo la app
    app = create_app()
    # 2. La pongo en modo 'TESTING' para que sepa que no es producción (ej: muestra mejores errores)
    app.config["TESTING"] = True

    # 3. Creo el cliente de prueba
    with app.test_client() as client:
        # 'yield' es como un return, pero se queda esperando.
        # Entrega el cliente al test, deja que el test corra, y luego (si hubiera código abajo) limpiaría todo.
        yield client


# TEST 1: Verificar que la lista inicia vacía
def test_get_alistamientos_empty(client):
    # Uso el 'client' que me entregó la fixture de arriba automáticamente.
    response = client.get("/alistamientos")

    # Verifico que la respuesta sea exitosa (200 OK) y que sea una lista vacía [].
    assert response.status_code == 200
    assert response.get_json() == []


# TEST 2: Camino feliz (Happy Path) - Crear correctamente
def test_create_alistamiento_success(client):
    # Preparo un JSON con TODOS los datos necesarios.
    payload = {
        "placa": "XYZ999",
        "mecanico": "Pedro",
        "fecha": "2026-02-16",
        "frenos_ok": True,
        "luces_ok": True,
        "aceite_ok": True,
        "llantas_ok": True,
        "observaciones": "Todo en buen estado",
    }

    # Envío los datos con POST.
    response = client.post("/alistamientos", json=payload)

    # Verifico que se creó (201 Created).
    assert response.status_code == 201

    # Reviso que la respuesta contenga la placa que envié.
    data = response.get_json()
    assert data["placa"] == "XYZ999"


# TEST 3: Manejo de errores - Faltan datos
def test_create_alistamiento_missing_fields(client):
    # Envío un JSON incompleto (solo la placa), faltan mecánico y fecha.
    payload = {"placa": "AAA111"}

    response = client.post("/alistamientos", json=payload)

    # El sistema debería rechazarlo con un error 400 (Bad Request).
    # Esto prueba que mis validaciones "if not ..." en las rutas funcionan.
    assert response.status_code == 400


# TEST 4: Borrar un registro existente
def test_delete_alistamiento_success(client):
    # Paso 1: Primero tengo que CREAR algo para poder borrarlo.
    payload = {
        "placa": "DEL123",
        "mecanico": "Ana",
        "fecha": "2026-02-16",
        "frenos_ok": True,
        "luces_ok": True,
        "aceite_ok": True,
        "llantas_ok": True,
        "observaciones": "OK",
    }
    client.post("/alistamientos", json=payload)

    # Paso 2: Ahora sí intento borrarlo usando la placa.
    response = client.delete("/alistamientos/DEL123")

    # Paso 3: Verifico que devuelva 204 (No Content), que significa borrado exitoso.
    assert response.status_code == 204


# TEST 5: Intentar borrar algo que no existe
def test_delete_alistamiento_not_found(client):
    # Intento borrar una placa inventada.
    response = client.delete("/alistamientos/NOEXISTE")

    # El sistema debe avisarme que no lo encontró con un 404 (Not Found).
    assert response.status_code == 404
