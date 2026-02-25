from flask import Blueprint, jsonify, request

# Importo mis propias funciones que hice en la carpeta de servicios.
# Así separo la lógica (cálculos) de las rutas (internet).
from app.services.citas_service import crear_cita, obtener_citas

# Creo un "Blueprint" (plano).
# Esto me sirve para agrupar todas las rutas que tienen que ver con 'citas' en un solo lugar
# y no tener todo amontonado en el archivo main.py.
citas_bp = Blueprint("citas", __name__)


# 1. RUTA PARA VER TODAS LAS CITAS
# Cuando alguien entre a la dirección '/citas' usando GET (navegador), ejecuto esto.
@citas_bp.route("/citas", methods=["GET"])
def listar_citas():
    # Llamo a mi servicio para obtener la lista y la convierto en JSON
    # para que el navegador o el frontend la entienda.
    return jsonify(obtener_citas())


# 2. RUTA PARA CREAR UNA CITA
# Esta ruta espera que le envíen datos (POST), no solo que la visiten.
@citas_bp.route("/citas", methods=["POST"])
def agendar_cita():
    # Recibo los datos que vienen en formato JSON desde el formulario o Postman.
    data = request.get_json()

    # Saco cada dato individualmente para revisarlos.
    cliente = data.get("cliente")
    fecha = data.get("fecha")
    hora = data.get("hora")

    # Validación básica: Si falta alguno de los datos obligatorios...
    if not cliente or not fecha or not hora:
        # ...devuelvo un error 400 (Bad Request) avisando qué pasó.
        return jsonify({"error": "Datos incompletos"}), 400

    # Si todo está bien, llamo al servicio para que cree el objeto Cita y lo guarde en la lista.
    cita_objeto = crear_cita(cliente, fecha, hora)

    # Devuelvo la cita creada convertida a diccionario y un código 201 (Created).
    # El 201 es el estándar para decir "se creó algo nuevo con éxito".
    return jsonify(cita_objeto.to_dict()), 201


# 3. RUTA PARA ELIMINAR UNA CITA
# Esta ruta recibe una variable '<nombre>' directamente en la URL.
@citas_bp.route("/citas/<nombre>", methods=["DELETE"])
def borrar_cita(nombre):
    # Importo la función de eliminar aquí mismo.
    from app.services.citas_service import eliminar_cita_servicio

    # Le paso el nombre que recibí en la URL al servicio para que actualice la lista.
    eliminar_cita_servicio(nombre)

    # Devuelvo un mensaje de éxito con código 200 (OK).
    return jsonify({"status": "success", "message": "Cita eliminada"}), 200
