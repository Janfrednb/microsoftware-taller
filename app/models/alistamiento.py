class Alistamiento:
    def __init__(self, placa, mecanico, fecha, frenos_ok, luces_ok, aceite_ok, llantas_ok, observaciones):
        self.placa = placa
        self.mecanico = mecanico
        self.fecha = fecha
        self.frenos_ok = frenos_ok
        self.luces_ok = luces_ok
        self.aceite_ok = aceite_ok
        self.llantas_ok = llantas_ok
        self.observaciones = observaciones

    def to_dict(self):
        return {
            "placa": self.placa,
            "mecanico": self.mecanico,
            "fecha": self.fecha,
            "frenos_ok": self.frenos_ok,
            "luces_ok": self.luces_ok,
            "aceite_ok": self.aceite_ok,
            "llantas_ok": self.llantas_ok,
            "observaciones": self.observaciones
        }
