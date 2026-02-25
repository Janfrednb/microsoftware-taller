# Traigo la clase Alistamiento para poder crear los objetos con los datos del vehículo.
from app.models.alistamiento import Alistamiento

# Igual que en citas, uso esta lista vacía para guardar los alistamientos en memoria.
# Es mi "base de datos" temporal mientras aprendo a conectar una real.
alistamientos = []


# Función para guardar un nuevo alistamiento (revisión).
# Recibe todos los datos, desde la placa hasta los estados de los frenos, luces, etc.
def crear_alistamiento(
    placa, mecanico, fecha, frenos_ok, luces_ok, aceite_ok, llantas_ok, observaciones
):
    # Creo el objeto usando la clase que importé arriba.
    nuevo_alistamiento = Alistamiento(
        placa,
        mecanico,
        fecha,
        frenos_ok,
        luces_ok,
        aceite_ok,
        llantas_ok,
        observaciones,
    )
    # Lo agrego a la lista para que quede guardado en el sistema.
    alistamientos.append(nuevo_alistamiento)

    # Devuelvo el objeto creado por si necesito usarlo inmediatamente.
    return nuevo_alistamiento


# Función para obtener todas las revisiones que he guardado.
def obtener_alistamientos():
    # Recorro la lista y convierto cada objeto a diccionario.
    # Esto es necesario para poder enviarlos a la plantilla HTML o verlos como JSON.
    return [alistamiento.to_dict() for alistamiento in alistamientos]


# Función para buscar una revisión específica usando la placa del carro.
def obtener_alistamiento_por_placa(placa):
    # Recorro uno por uno los alistamientos que tengo en la lista.
    for alistamiento in alistamientos:
        # Si la placa del alistamiento actual coincide con la que estoy buscando...
        if alistamiento.placa == placa:
            return alistamiento  # ...devuelvo ese objeto específico.

    # Si termino el bucle y no encontré nada, devuelvo None (vacío).
    return None


# Función para borrar una revisión específica.
def eliminar_alistamiento_por_placa(placa):
    # Busco en la lista cuál coincide con la placa.
    for alistamiento in alistamientos:
        if alistamiento.placa == placa:
            # Si lo encuentro, uso .remove() que es un método de las listas de Python para sacarlo.
            alistamientos.remove(alistamiento)
            return True  # Retorno True para avisar que sí se borró.

    # Si no encontré la placa, retorno False para avisar que no se hizo nada.
    return False
