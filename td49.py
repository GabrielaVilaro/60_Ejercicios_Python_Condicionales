#coding=UTF-8


'''
Ejercicio: 49, Tema: Toma de desiciones
Enunciado --> (49.)Realizar un algoritmo que lea las 3 notas de un alumno e informe si está aprobado o desaprobado,
considerando que se aprueba si su promedio es, por lo menos, 4.
Nombre del archivo 'td49.py'
Desarrollo del algoritmo en código Python
'''

nota_1 = raw_input("\nIngrese la primer nota del alumno: ")
nota_1 = int(nota_1)
nota_2 = raw_input("\nIngrese la segunda nota del alumno: ")
nota_2 = int(nota_2)
nota_3 = raw_input("\nIngrese la tercer nota del alumno: ")
nota_3 = int(nota_3)

total = nota_1 + nota_2 + nota_3
promedio = total / 3

if promedio >= 4:
	print "\nEl alumno se encuentra en condición de APROBADO."
else:
	print "\nEl alumno se encuentra en condición de DESAPROBADO."

raw_input("\nOrpima la tecla ENTER para finalizar.")