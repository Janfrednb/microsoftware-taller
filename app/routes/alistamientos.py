from flask import Blueprint, jsonify, request

# Importo las funciones específicas del servicio de alistamientos.
# Hago esto para mantener la lógica separada: aquí solo manejo rutas, allá los cálculos.
from app.services.alistamientos_service import (
    crear_alistamiento,
    obtener_alistamientos,
    obtener_alistamiento_por_placa,
    eliminar_alistamiento_por_placa,
)

# Defino el Blueprint para "alistamientos".
# Esto permite que mi aplicación sea modular y no tenga todo el código en un solo archivo gigante.
alistamientos_bp = Blueprint("alistamientos", __name__)


# RUTA 1: Obtener todos los alistamientos
@alistamientos_bp.route("/alistamientos", methods=["GET"])
def listar_alistamientos():
    # Llamo al servicio para obtener la lista y la envío como respuesta JSON al navegador.
    return jsonify(obtener_alistamientos())


# RUTA 2: Crear un nuevo alistamiento
@alistamientos_bp.route("/alistamientos", methods=["POST"])
def registrar_alistamiento():
    # Obtengo los datos que me envían en el cuerpo de la petición (JSON).
    data = request.get_json()

    # Extraigo cada campo del diccionario para validarlo o usarlo.
    placa = data.get("placa")
    mecanico = data.get("mecanico")
    fecha = data.get("fecha")
    frenos_ok = data.get("frenos_ok")
    luces_ok = data.get("luces_ok")
    aceite_ok = data.get("aceite_ok")
    llantas_ok = data.get("llantas_ok")
    observaciones = data.get("observaciones")

    # Validación básica: Reviso que los datos obligatorios existan.
    # Si falta la placa, el mecánico o la fecha, devuelvo un error 400 (Bad Request).
    if not placa or not mecanico or not fecha:
        return jsonify({"error": "Datos incompletos"}), 400

    # Si todo está bien, llamo a la función del servicio para crear el objeto.
    alistamiento = crear_alistamiento(
        placa,
        mecanico,
        fecha,
        frenos_ok,
        luces_ok,
        aceite_ok,
        llantas_ok,
        observaciones,
    )

    # Devuelvo el objeto creado y un código 201, que significa "Creado exitosamente".
    return jsonify(alistamiento.to_dict()), 201


# RUTA 3: Buscar un alistamiento específico por PLACA
# La parte <placa> en la URL es una variable dinámica.
@alistamientos_bp.route("/alistamientos/<placa>", methods=["GET"])
def obtener_por_placa(placa):
    # Busco en el servicio usando la placa que recibí en la URL.
    alistamiento = obtener_alistamiento_por_placa(placa)

    # Si el servicio me devuelve None (no encontró nada), respondo con un error 404 (Not Found).
    if not alistamiento:
        return jsonify({"error": "Alistamiento no encontrado"}), 404

    # Si lo encontró, devuelvo los datos y un código 200 (OK).
    return jsonify(alistamiento.to_dict()), 200


# RUTA 4: Eliminar por PLACA
@alistamientos_bp.route("/alistamientos/<placa>", methods=["DELETE"])
def eliminar_por_placa(placa):
    # Intento eliminar usando el servicio. Me devolverá True si pudo, o False si no existía.
    eliminado = eliminar_alistamiento_por_placa(placa)

    # Si no se pudo eliminar porque no existía, devuelvo 404.
    if not eliminado:
        return jsonify({"error": "Alistamiento no encontrado"}), 404

    # Si se eliminó correctamente, devuelvo una cadena vacía "" y el código 204 (No Content).
    # El 204 es el estándar para decir "se hizo la acción pero no tengo nada que mostrarte".
    return "", 204
