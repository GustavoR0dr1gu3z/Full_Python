from teclado import Teclado
from raton import Raton
from monitor import Monitor
from computadora import Computadora

# OBJETO 1
t1 = Teclado('HP', 'USB')        
r1 = Raton('HP', 'USB')
m1 = Monitor('HP',15)

c1 = Computadora('HP',m1,t1,r1)
print(c1)

# OBJETO 2
t2 = Teclado('Acer', 'Bluetooth')        
r2 = Raton('Acer', 'Bluetooth')
m2 = Monitor('Acer',27)

c2 = Computadora('Acer',m2,t2,r2)
print(c2)     

compus = [c1, c2]