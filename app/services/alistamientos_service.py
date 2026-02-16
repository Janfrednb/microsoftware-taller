from app.models.alistamiento import Alistamiento

# almacenamiento en memoria (mock)
alistamientos = []

def crear_alistamiento(placa, mecanico, fecha, frenos_ok, luces_ok, aceite_ok, llantas_ok, observaciones):
    nuevo_alistamiento = Alistamiento(
        placa,
        mecanico,
        fecha,
        frenos_ok,
        luces_ok,
        aceite_ok,
        llantas_ok,
        observaciones
    )
    alistamientos.append(nuevo_alistamiento)
    return nuevo_alistamiento

def obtener_alistamientos():
    return [alistamiento.to_dict() for alistamiento in alistamientos]


def obtener_alistamiento_por_placa(placa):
    for alistamiento in alistamientos:
        if alistamiento.placa == placa:
            return alistamiento
    return None


def eliminar_alistamiento_por_placa(placa):
    for alistamiento in alistamientos:
        if alistamiento.placa == placa:
            alistamientos.remove(alistamiento)
            return True
    return False
