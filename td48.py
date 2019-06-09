#coding=UTF-8


'''
Ejercicio: 48, Tema: Toma de desiciones
Enunciado --> (48.)Desarrollar un algoritmo que lea 2 datos numéricos que representan la cantidad de varones y la
cantidad de mujeres de un curso e imprimir:
48.1. La cantidad total de alumnos de la clase.
48.2. El porcentaje de mujeres y el porcentaje de varones.
Nombre del archivo 'td48.py'
Desarrollo del algoritmo en código Python
'''
mujeres = raw_input("\nIngrese la cantidad de mujeres: ")
mujeres = float(mujeres)
varones = raw_input("\nIngrese la cantidad de varones: ")
varones = float(varones)


def porcentaje(parte, todo):
	return	parte / todo * 100

total = mujeres + varones

print "\nLa cantidad total de alumnos es de: ", total

print "\nEl porcentaje de mujeres es de: %", porcentaje(mujeres, total)
print "\nEl porcentaje de varones es de: %", porcentaje(varones, total)