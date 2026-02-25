# Importo la clase Cita desde los modelos para poder crear objetos de este tipo.
from app.models.cita import Cita

# Creo una lista vacía llamada 'citas'.
# Como no tengo base de datos todavía, usaré esta lista para guardar la información en la memoria RAM.
# Si reinicio el programa, esto se borra (es un mock).
citas = []


# Función para registrar una nueva cita en el sistema.
def crear_cita(cliente, fecha, hora):
    # Primero creo el objeto Cita con los datos que recibo.
    nueva_cita = Cita(cliente, fecha, hora)

    # Agrego esa nueva cita a mi lista (mi "base de datos" temporal).
    citas.append(nueva_cita)

    # Devuelvo el objeto creado por si necesito confirmar los datos.
    return nueva_cita


# Función para consultar todas las citas que existen.
def obtener_citas():
    # Aquí uso una comprensión de lista (list comprehension).
    # Recorro cada cita en la lista y la convierto a diccionario con .to_dict().
    # Hago esto para que al devolver los datos, sea fácil enviarlos como JSON o mostrarlos en la web.
    return [cita.to_dict() for cita in citas]


# Función para borrar una cita buscando por el nombre del cliente.
def eliminar_cita_servicio(nombre_cliente):
    # Uso 'global' para avisarle a Python que voy a modificar la lista 'citas' que está afuera de la función.
    global citas

    # En lugar de buscar y borrar, lo que hago es crear una lista nueva filtrada.
    # Me quedo con todas las citas donde el cliente sea DIFERENTE al que quiero borrar.
    # Así, la cita que coincida con 'nombre_cliente' desaparece de la lista.
    citas = [c for c in citas if c.cliente != nombre_cliente]

    # Devuelvo True para confirmar que el proceso se hizo.
    return True
