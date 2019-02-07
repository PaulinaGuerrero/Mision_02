# Autor: Paulina Guerrero Ruiz, a01024519
#  Calcula la distancia entre dos puntos

x1 = int(input("Teclea x1: "))
y1 = int(input("Teclea y1: "))
x2 = int(input("Teclea x2: "))
y2 = int(input("Teclea y2: "))

d = (((x2-x1) **2) +((y2-y1) **2) **0.5)

print("distancia entre dos puntos: %.3f" % (d))