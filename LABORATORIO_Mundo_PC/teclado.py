from dispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclado = 0

    def __init__(self):
        Teclado.contador_teclado +=1
        self._id