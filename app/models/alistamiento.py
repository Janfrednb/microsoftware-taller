# Creo una clase para representar los alistamientos (revisiones) de los vehículos.
# Esto me permite manejar cada revisión como un objeto ordenado.
class Alistamiento:
    
    # Este es el método inicializador. Se ejecuta cada vez que creo un nuevo alistamiento.
    # Recibo aquí todos los datos que vienen del formulario o del sistema.
    def __init__(self, placa, mecanico, fecha, frenos_ok, luces_ok, aceite_ok, llantas_ok, observaciones):
        self.placa = placa          # Guardo la placa del vehículo en el objeto
        self.mecanico = mecanico    # Guardo el nombre del mecánico responsable
        self.fecha = fecha          # Guardo la fecha de la revisión
        
        # Guardo el estado de cada parte (probablemente True o False si pasó la revisión)
        self.frenos_ok = frenos_ok
        self.luces_ok = luces_ok
        self.aceite_ok = aceite_ok
        self.llantas_ok = llantas_ok
        
        self.observaciones = observaciones # Guardo las notas adicionales que escriba el mecánico

    # Creo este método para convertir la información del objeto en un diccionario simple.
    # Esto es necesario para poder mostrar los datos fácilmente en la página web o en formato JSON.
    def to_dict(self):
        return {
            "placa": self.placa,             # Asocio la clave "placa" con su valor
            "mecanico": self.mecanico,       # Asocio el mecánico
            "fecha": self.fecha,             # La fecha
            "frenos_ok": self.frenos_ok,     # Estado de frenos
            "luces_ok": self.luces_ok,       # Estado de luces
            "aceite_ok": self.aceite_ok,     # Estado de aceite
            "llantas_ok": self.llantas_ok,   # Estado de llantas
            "observaciones": self.observaciones # Las notas finales
        }
