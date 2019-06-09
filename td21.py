#coding=UTF-8


'''
Ejercicio: 21, Tema: Toma de desiciones
Enunciado --> (21.) Se ingresan dos números informar el menor.
Nombre del archivo 'td21.py'
Desarrollo del algoritmo en código Python
'''
print "Recibe dos númerps e informa el menor."

num1 = raw_input("\nIngrese un número: ")
num1 = int(num1)
num2 = raw_input("\nIngrese otro número: ")
num2 = int(num2)

if num1 > num2:
	print "\nEl número menor es el segundo."
else:
	print "\nEl número menor es el primero."
raw_input("\nOprima la tecla ENTER para finalizar.")
