from app.models.cita import Cita

# almacenamiento en memoria (mock)
citas = []

def crear_cita(cliente, fecha, hora):
    nueva_cita = Cita(cliente, fecha, hora)
    citas.append(nueva_cita)
    return nueva_cita

def obtener_citas():
    return [cita.to_dict() for cita in citas]

def eliminar_cita_servicio(nombre_cliente):
    global citas
    # Mantenemos todas las citas EXCEPTO la que coincide con el nombre
    citas = [c for c in citas if c.cliente != nombre_cliente]
    return True
