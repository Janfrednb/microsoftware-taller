class Cita:
    def __init__(self, cliente, fecha, hora):
        self.cliente = cliente
        self.fecha = fecha
        self.hora = hora

    def to_dict(self):
        return {
            "cliente": self.cliente,
            "fecha": self.fecha,
            "hora": self.hora
        }
