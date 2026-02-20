from flask import Blueprint, jsonify, request
from app.services.citas_service import crear_cita, obtener_citas

citas_bp = Blueprint("citas", __name__)

# 1. RUTA PARA VER TODAS LAS CITAS
@citas_bp.route("/citas", methods=["GET"])
def listar_citas():
    return jsonify(obtener_citas())

# 2. RUTA PARA CREAR UNA CITA
@citas_bp.route("/citas", methods=["POST"])
def agendar_cita():
    data = request.get_json()

    cliente = data.get("cliente")
    fecha = data.get("fecha")
    hora = data.get("hora")

    if not cliente or not fecha or not hora:
        return jsonify({"error": "Datos incompletos"}), 400

    # El servicio crea el objeto Cita
    cita_objeto = crear_cita(cliente, fecha, hora)
    
    # Devolvemos el objeto convertido a diccionario
    return jsonify(cita_objeto.to_dict()), 201

# 3. RUTA PARA ELIMINAR UNA CITA
@citas_bp.route("/citas/<nombre>", methods=["DELETE"])
def borrar_cita(nombre):
    from app.services.citas_service import eliminar_cita_servicio
    
    # Ejecutamos la eliminación en el servicio
    eliminar_cita_servicio(nombre)
    
    return jsonify({"status": "success", "message": "Cita eliminada"}), 200
