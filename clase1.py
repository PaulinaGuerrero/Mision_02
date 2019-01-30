# Autor: paulina guerrero Ruiz A01024519
# Calcular porcentajes

print("Cantidad de mujeres inscritas")
m = int(input("Teclea el numero de mujeres inscritas: "))

print("Cantidad de hombres inscritos")
h = int(input("Teclea el numero de hombres inscritos: "))

t = (m+h)

m1 = (m/t)*100
h1 = (h/t)*100

print("Total de alumnos inscritos: ", (t))
print("Porcentaje de mujeres: %.1f "% (m1))
print ("porcenatje de hombres: %.1f" % (h1))

