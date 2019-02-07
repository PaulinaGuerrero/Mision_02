# Autor: Paulina Guerrero Ruiz, A01024519
# Resuelve problema de velocidad
print("velocidad del auto en km/h ")
v = int(input("Teclea la velocidad: "))

d1 = (v*6)
d2 = (v*3.5)

t1 = (485/v)

print("Distancia recorrida en 6 hrs: %.1f" % (d1))
print( "Distancia recorrida en 3.5 hrs: %.1f" % (d2))
print("Tiempo para recorrer 485 km: %.1f" % (t1))

