#coding=UTF-8


'''
Ejercicio: 38, Tema: Toma de desiciones
Enunciado --> (38.)Ingresar un número e informar si es par o impar.
Nombre del archivo 'td38.py'
Desarrollo del algoritmo en código Python
'''
print "\nRecibe un número e informa si es par o impar."

numero = raw_input("\nIngrese un número: ")
numero = int(numero)

if numero % 2 == 0:
	print "\nEl número ingresado es par."
else:
	print "\nEl número ingresado es impar."

raw_input("\nOprima la tecla ENTER para finalizar.")