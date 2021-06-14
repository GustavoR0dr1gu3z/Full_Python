from dispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):

    contadorRaton = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contadorRaton += 1
        self._id_raton = Raton.contadorRaton
        super().__init__(marca,tipo_entrada)


    def __str__(self):
        return "ID Raton: {}, Marca: {}, Tipo_Entrada: {}".format(self._id_raton, self.marca, self.tipo_entrada)


'''
# Objetos de prueba
if __name__ == '__main__':
    r1 = Raton('HP', 'USB')
    print(r1)

'''