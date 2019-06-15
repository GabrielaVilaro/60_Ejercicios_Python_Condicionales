#coding=UTF-8

"""Ejercicio: 3, Tema: Repeticiones, bucles e iteraciones.
Enunciado --> (3.) Se ingresa una lista de N números y de ellos se desea obtener:
3.1. Cantidad total de números ingresados.
3.2. Cantidad de números negativos ingresados.
3.3. Cantidad de números positivos ingresados.
3.4. Promedio de los positivos.
3.5. Promedio de los negativos.
3.6. El mayor y el menor número ingresado.
Nombre del archivo 'b3.py'
Desarrollo del algoritmo en código Python
"""

promedio = 0
suma = 0
n = raw_input("Ingrese la cantidad de números a calcular: ")
n = int(n)
cant = 0
negativos = 0
positivos = 0
pn = 0
pp = 0
while cant < n:
	m = raw_input("Ingrese un número: ")
	m = int(m)
	suma = suma + m
	cant = cant + 1
	if m > 0:
		positivos = positivos + 1
	if m < 0:
		negativos = negativos + 1
promedio = suma / n
pn = negativos / n
pp = positivos / n
print "El promedio es: ", promedio
print "La suma es: ", suma
print "Positivos: ", positivos
print "Negativos: ", negativos
print "Promedio de negativos: ", pn
print "Promedio de positivos: ", pp

raw_input("Oprima ENTER para finalizar el programa.")
