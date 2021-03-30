class Persona:
    def __init__(self, nombre, apPaterno, apMaterno):
        self.nombre = nombre        #Sin guion bajo: Publico
        self._apPaterno = apPaterno  #1 guion bajo: Protected
        self.__apMaterno = apMaterno  #2 guion bajo: Privado

    def metodo_publico(self):
        self.__metodo_privado()

    # Definir un metodo privado
    def __metodo_privado(self):
        print(self.nombre)
        print(self._apPaterno)
        print(self.__apMaterno)

    def get_apMaterno(self):
        return self.__apMaterno
    
    def set_apMaterno(self, apMaterno):
        self.__apMaterno = apMaterno

p1 = Persona("Gustavo", "Rodriguez", "Calzada")    
# p1.__metodo_privado() No se puede acceder, debido a ser un metodo privado
p1.metodo_publico() # Se crea un metodo publico, llamando al metodo privado
print("\n")
print(p1.nombre)
print(p1._apPaterno)
print(p1.get_apMaterno())