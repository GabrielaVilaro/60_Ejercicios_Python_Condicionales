#coding=UTF-8


'''
Ejercicio: 57, Tema: Toma de desiciones
Enunciado --> (57.)Leer 2 valores decimales y mostrar el mayor de ellos.
Nombre del archivo 'td57.py'
Desarrollo del algoritmo en código Python
'''

decimal1 = raw_input("\nIngrese el primer número decimal: ")
decimal1 = float(decimal1)

decimal2 = raw_input ("\nIngrese el segundo número decimal: ")
decimal2 = float(decimal2)

if decimal1 > decimal2:
	print "\nEl mayor es: ", decimal1
else:
	print "\nEl mayor es: ", decimal2

raw_input("\nOprima ENTER para finalizar.")
