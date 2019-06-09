#coding=UTF-8


'''
Ejercicio: 39, Tema: Toma de desiciones
Enunciado --> (39.)Se tiene un número N, informar si es par y múltiplo de 7.
Nombre del archivo 'td39.py'
Desarrollo del algoritmo en código Python
'''
print "\nRecibe un número e informa si es par y múltiplo de 7."

numero = raw_input("\nIngrese un número: ")
numero = int(numero)

if numero % 2 == 0:
	print "\nEl número ingresado es par"
if numero % 7 == 0:
	print "\nEl número ingresado es múltiplo de 7."
	
raw_input("\nOprima la tecla ENTER para finalizar.")