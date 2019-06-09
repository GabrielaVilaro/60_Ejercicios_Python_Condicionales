#coding=UTF-8


'''
Ejercicio: 44, Tema: Toma de desiciones
Enunciado --> (44.) Ingresar un número e informar si es múltiplo de 6 y no de 9.
Nombre del archivo 'td44.py'
Desarrollo del algoritmo en código Python
'''

numero = raw_input("\nIngrese un número: ")
numero = int(numero)

if numero % 6 == 0:
	print "\nEl número ingresado es múltiplo de 6."
else:
	if numero % 9 != 0:
		print "\nEl número ingresado NO es múltiplo de 9."

raw_input("\nOprima ENTER para finalizar.")