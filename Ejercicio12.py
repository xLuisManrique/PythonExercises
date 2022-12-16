# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
# Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace
# por no ser fresca y el coste final total.

barras = int(input("Introduce el número de barras vendidas que no son frescas: "))
precio_barras = 3.49
descuento = 0.6
costo = barras * precio_barras * (1 - descuento)
print("El precio de una barra fresca es: " + str(precio_barras) + "€")
print("El descuento sobre una barra no fresca es: " + str(descuento * 100) + "%")
print("Precio a pagar con descuento es: " + str(round(costo, 2)) + "€")
