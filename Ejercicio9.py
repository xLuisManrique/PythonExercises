# Escribir un programa que pregunte al usuario una cantidad a invertir,el interés anual
# y el número de años,y muestre por pantalla el capital obtenido en la inversión.

inversion = float(input("Cuanto desea invertir? "))
interes = float(input("Cual es la tasa de interes porcentual anual: "))
anios = int(input("A cuantos años? "))
capital = str(round(inversion * ( interes / 100 + 1) ** anios, 2))
print("Capital final: " + capital)