#coding=UTF-8

'''
Ejercicio: 2, Tema: Repeticiones, bucles e iteraciones.
Enunciado --> (2.) Se ingresan al proceso N números, se desea de los N números ingresados obtener la sumatoria, el
promedio y la cantidad de números ingresados.
Nombre del archivo 'b2.py'
Desarrollo del algoritmo en código Python
'''

promedio = 0
suma = 0
n = raw_input("Ingrese la cantidad de números a calcular: ")
n = int(n)
cant = 0
while cant < n:
	m = raw_input("Ingrese un número: ")
	m = int(m)
	suma = suma + m
	cant = cant + 1
promedio = suma / n
print "El promedio es: ", promedio
print "La suma es: ", suma
raw_input("Oprima ENTER para finalizar el programa.")
