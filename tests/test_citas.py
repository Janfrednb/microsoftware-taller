import json

# Importo la función que crea mi aplicación Flask.
# Esto es necesario para iniciar una versión "limpia" de la app para cada prueba.
from app.main import create_app


# TEST 1: Verificar que la lista empieza vacía.
# Es una prueba básica para asegurar que la ruta GET responde bien aunque no haya datos.
def test_get_citas_vacio():
    # 1. Configuración (Setup)
    app = create_app()

    # Creo un "cliente de prueba".
    # Es como un navegador falso que Flask me presta para hacer peticiones sin abrir Chrome.
    client = app.test_client()

    # 2. Ejecución (Action)
    # Le digo a mi cliente falso que vaya a la ruta "/citas" usando GET.
    response = client.get("/citas")

    # 3. Verificación (Assert)
    # Compruebo que el código de estado sea 200 (OK).
    assert response.status_code == 200
    # Compruebo que la respuesta sea una lista vacía [], ya que no he guardado nada aún.
    assert response.json == []


# TEST 2: Verificar que puedo crear una cita.
# Esta prueba asegura que la ruta POST recibe datos y los guarda correctamente.
def test_post_citas_crea_cita():
    # 1. Configuración
    app = create_app()
    client = app.test_client()

    # Preparo los datos falsos que voy a enviar.
    nueva_cita = {"cliente": "Test Cliente", "fecha": "2026-02-11", "hora": "09:00"}

    # 2. Ejecución
    # Envío los datos a la ruta "/citas" usando POST.
    response = client.post(
        "/citas",
        data=json.dumps(nueva_cita),  # Convierto mi diccionario de Python a texto JSON.
        content_type="application/json",  # Le aviso al servidor que le estoy enviando JSON.
    )

    # 3. Verificación
    # Espero un código 201 (Created), que es el estándar para creación exitosa.
    assert response.status_code == 201

    # Verifico que el servidor me devuelva el mismo nombre de cliente que envié.
    # Esto me confirma que los datos viajaron y volvieron bien.
    assert response.json["cliente"] == "Test Cliente"
