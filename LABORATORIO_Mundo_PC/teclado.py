from dispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclado = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclado +=1
        self._id_teclado = Teclado.contador_teclado
        super().__init__(marca, tipo_entrada)
