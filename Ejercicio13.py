# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla
# en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre = input("Cuàl es tu nombre: ")
reps = int(input("Cuantas veces quiere que se repita tu nombre: "))
print((nombre + "\n") * int(reps))
