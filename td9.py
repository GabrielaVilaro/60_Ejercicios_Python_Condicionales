#coding=UTF-8


'''
Ejercicio: 9, Tema: Toma de desiciones
Enunciado --> (9.) Construir un algoritmo que permita leer un número entero y determinar si es de 2 dígitos.
Nombre del archivo 'td9.py'
Desarrollo del algoritmo en código Python
'''

num = raw_input("\nIngrese un número entero: ")
num = int (num)

if num > 9 and num < 99: 
	print "\nEl número ingresado es de 2 (dos) digitos."
else:
	print "\n\nEl número ingresado NO es de 2 (dos) dígitos."

raw_input("\t\n\nOprima la tecla ENTER para salir.")
