# Autor: Paulina Guerrero Ruiz, A01024519
# Saca las cuentas del usuario

print("Subtotal de la Comida")
c = int(input("Teclea el total de tu comida:"))

p =((c*13)/100)
i =((c*16)/100)
f = ((c+p)+(c+i)-c)

print("Costo de su comida: ",c)
print("Propina: %.2f" % (p))
print("IVA: %.2f" % (i))
print("Tota a pagar: %.2f" % (f))

