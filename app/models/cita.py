# Defino la clase Cita para representar las citas de los clientes en el sistema.
# Esto me sirve para manejar cada cita como un objeto individual.
class Cita:

    # Este es el constructor. Se ejecuta cuando creo una nueva cita.
    # Recibe los datos básicos: quién es el cliente, qué día y a qué hora es.
    def __init__(self, cliente, fecha, hora):
        self.cliente = cliente  # Guardo el nombre del cliente en el objeto
        self.fecha = fecha  # Guardo la fecha de la cita
        self.hora = hora  # Guardo la hora acordada

    # Creo este método para convertir los datos de la cita en un diccionario.
    # Esto es útil porque Flask maneja mejor los diccionarios para enviar respuestas JSON o mostrarlas en la web.
    def to_dict(self):
        return {
            "cliente": self.cliente,  # La clave 'cliente' tendrá el valor guardado
            "fecha": self.fecha,  # La fecha de la cita
            "hora": self.hora,  # La hora de la cita
        }
