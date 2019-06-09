#coding=UTF-8


'''
Ejercicio: 36, Tema: Toma de desiciones
Enunciado --> (36.)Se ingresa la primera letra de los apellidos de tres alumnos. Informarlas en forma ordenada
ascendente sin hacer intercambio de valores.
Nombre del archivo 'td36.py'
Desarrollo del algoritmo en código Python
'''
alumno1 = raw_input("\nIngrese la primer letra de apellido del primer alumno: ")
alumno2 = raw_input("\nIngrese la primer letra de apellido del segundo alumno: ")
alumno3 = raw_input("\nIngrese la primer letra de apellido del tercer alumno: ")

apellidos_alumnos = [alumno1, alumno2, alumno3]

for x in sorted(apellidos_alumnos):
	print x

raw_input("\nOprima la tecla ENTER para finalizar.")
