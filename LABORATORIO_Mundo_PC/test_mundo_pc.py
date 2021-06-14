from teclado import Teclado
from raton import Raton
from monitor import Monitor
from computadora import Computadora
from orden import Orden


# OBJETO 1
t1 = Teclado('HP', 'USB')        
r1 = Raton('HP', 'USB')
m1 = Monitor('HP',15)
c1 = Computadora('HP',m1,t1,r1)

# OBJETO 2
t2 = Teclado('Acer', 'Bluetooth')        
r2 = Raton('Acer', 'Bluetooth')
m2 = Monitor('Acer',27)
c2 = Computadora('Acer',m2,t2,r2)

# OBJETO 3
t3 = Teclado('Patito', 'Bluetooth')        
r3 = Raton('Patito', 'USB')
m3 = Monitor('Patito',50)
c3 = Computadora('Patito',m3,t3,r3)

# OBJETO 4
t4 = Teclado('Guena', 'USB')        
r4 = Raton('Guena', 'Bluetooth')
m4 = Monitor('Guena',27)
c4 = Computadora('Guena',m4,t4,r4)


# Orden de las computadoras

# ORDEN 1
compus1 = [c1, c2]
orden1 = Orden(compus1)
print(orden1)

# ORDEN 2
compus2 = [c3, c4]
orden2 = Orden(compus2)
print(orden2)

# ORDEN 3
compus3 = [c1, c4]
orden3 = Orden(compus3)
print(orden3)

# ORDEN 4
compus4 = [c2, c3]
orden4 = Orden(compus4)
print(orden4)
