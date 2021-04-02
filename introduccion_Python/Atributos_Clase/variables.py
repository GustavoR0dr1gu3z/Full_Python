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

# A pesar de que no está listada en init, se puede acceder desde el objeto
print(objeto1.variable_clase)

# Accedemos a variables de clase cpn el nombre de la clase
print(MiClase.variable_clase)

# Objeto donde se modifica la variable de clase
objeto1.variable_clase = "Modificando variable de clase"
print(objeto1.variable_clase)

# Como solo se modificó desde el objeto, el valor sigue igual
print(MiClase.variable_clase)

objeto2 = MiClase("Nuevo valor de variable de instancia")
print(objeto2.variable_clase)

objeto3 = MiClase("Tercer objeto")
MiClase.variable_clase = "Cambio desde la clase"
print(objeto1.variable_clase)
print(objeto2.variable_clase)
print(objeto3.variable_clase)