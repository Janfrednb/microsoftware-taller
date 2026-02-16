from flask import Blueprint, jsonify, request
from app.services.alistamientos_service import (
    crear_alistamiento,
    obtener_alistamientos,
    obtener_alistamiento_por_placa,
    eliminar_alistamiento_por_placa
)

alistamientos_bp = Blueprint("alistamientos", __name__)

@alistamientos_bp.route("/alistamientos", methods=["GET"])
def listar_alistamientos():
    return jsonify(obtener_alistamientos())


@alistamientos_bp.route("/alistamientos", methods=["POST"])
def registrar_alistamiento():
    data = request.get_json()

    placa = data.get("placa")
    mecanico = data.get("mecanico")
    fecha = data.get("fecha")
    frenos_ok = data.get("frenos_ok")
    luces_ok = data.get("luces_ok")
    aceite_ok = data.get("aceite_ok")
    llantas_ok = data.get("llantas_ok")
    observaciones = data.get("observaciones")

    if not placa or not mecanico or not fecha:
        return jsonify({"error": "Datos incompletos"}), 400

    alistamiento = crear_alistamiento(
        placa,
        mecanico,
        fecha,
        frenos_ok,
        luces_ok,
        aceite_ok,
        llantas_ok,
        observaciones
    )

    return jsonify(alistamiento.to_dict()), 201


@alistamientos_bp.route("/alistamientos/<placa>", methods=["GET"])
def obtener_por_placa(placa):
    alistamiento = obtener_alistamiento_por_placa(placa)

    if not alistamiento:
        return jsonify({"error": "Alistamiento no encontrado"}), 404

    return jsonify(alistamiento.to_dict()), 200


@alistamientos_bp.route("/alistamientos/<placa>", methods=["DELETE"])
def eliminar_por_placa(placa):
    eliminado = eliminar_alistamiento_por_placa(placa)

    if not eliminado:
        return jsonify({"error": "Alistamiento no encontrado"}), 404

    return "", 204
