class MiClase:

    variable_clase = "Variable de Clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

# Se accede directamente a la variable de clase
print(MiClase.variable_clase)

# Se accede cuando se crea el objeto
objeto1 = MiClase("Variable de Instancia")
print(objeto1.variable_instancia)

# Ahora desde la clase
MiClase.variable_instancia="Variable de Instancia 2"
print(MiClase.variable_instancia)