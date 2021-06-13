from dispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):

    contadorRaton = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contadorRaton += 1
        self._id_raton = Raton.contadorRaton