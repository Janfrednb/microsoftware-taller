from flask import Blueprint, jsonify, request
from app.services.citas_service import crear_cita, obtener_citas

citas_bp = Blueprint("citas", __name__)

@citas_bp.route("/citas", methods=["GET"])
def listar_citas():
    return jsonify(obtener_citas())

@citas_bp.route("/citas", methods=["POST"])
def agendar_cita():
    data = request.get_json()

    cliente = data.get("cliente")
    fecha = data.get("fecha")
    hora = data.get("hora")

    if not cliente or not fecha or not hora:
        return jsonify({"error": "Datos incompletos"}), 400

    cita = crear_cita(cliente, fecha, hora)
    return jsonify(cita.to_dict()), 201

