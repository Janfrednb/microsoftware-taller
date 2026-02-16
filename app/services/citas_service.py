from app.models.cita import Cita

# almacenamiento en memoria (mock)
citas = []

def crear_cita(cliente, fecha, hora):
    nueva_cita = Cita(cliente, fecha, hora)
    citas.append(nueva_cita)
    return nueva_cita

def obtener_citas():
    return [cita.to_dict() for cita in citas]
