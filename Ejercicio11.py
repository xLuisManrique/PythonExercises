# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance
# final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero
# depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe
# calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
# Redondear cada cantidad a dos decimales.

interes = 0.04
dinero_inicial = float(input("Cuanto dinero deseas depositar: "))
anio_uno = dinero_inicial * ( 1 + interes)
anio_dos = anio_uno * ( 1 + interes)
anio_tres = anio_dos * ( 1 + interes)
print("Ahorra del primer año: " + str(round(anio_uno, 2)))
print("Ahorra del segundo año: " + str(round(anio_dos, 2)))
print("Ahorra del tercer año: " + str(round(anio_tres, 2)))
