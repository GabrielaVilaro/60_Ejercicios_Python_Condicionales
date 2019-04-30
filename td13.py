#coding=UTF-8


'''
Ejercicio: 13, Tema: Toma de desiciones
Enunciado --> (13.) Construir un algoritmo que permita leer un número entero y determinar si el número leído es par.
Nombre del archivo 'td13.py'
Desarrollo del algoritmo en código Python
'''
	
print "Debe ingresar un número entero."
num = raw_input ("\nIngrese un número: ")
num = int (num)

if num % 2 == 0:
	print "\nEl número ingresado es par."
else:
	print "\nEl número ingresado NO es par."
	
raw_input ("\nOprima ENTER para finalizar.")
