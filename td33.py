#coding=UTF-8


'''
Ejercicio: 33, Tema: Toma de desiciones
Enunciado --> (33.)Ingresar tres números. Informar:
33.1. En los números ingresados ¿Hay algún negativo?
33.2. En los números ingresados ¿Hay algún número que pertenezca al intervalo de valores que van
desde el 23 al 37?
Nombre del archivo 'td33.py'
Desarrollo del algoritmo en código Python
'''
print "\nRecibe 3 números e informa si hay negativos y que pertenezcan al intervalo del 23 al 37."
num1 = raw_input("\nIngresar el primer número: ")
num1 = int(num1)
num2 = raw_input("\nIngresar el segundo número: ")
num2 = int(num2)
num3 = raw_input("\nIngresar el tercer número: ")
num3 = int(num3)

if num1 < 0 or num2 < 0 or num3 < 0:
	print "\nHas ingresado por lo menos un número negativo."

if num1 >=23 and num1 <=37 or num2 >=23 and num2 <=37 or num3 >=23 and num3 <=37:
	print "\nHay por lo menos un número que pertece al intervalo de valores que van del 23 al 37."
	
raw_input("\nOprima la tecla ENTER para finalizar.")

