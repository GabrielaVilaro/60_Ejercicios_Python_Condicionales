#coding=UTF-8


'''
Ejercicio: 20, Tema: Toma de desiciones
Enunciado --> (20.) Escribir un programa que dado los tres lados de un triángulo: A, B y C determine de que tipo es.
Suponiendo que A sea el mayor de los lados, usar la siguiente tabla para la resolución del problema: si
A >= B + C entonces no forma un triángulo; si A2 = B2 + C2 entonces forma un triángulo rectangulo; si
A2 > B2 + C2 entonces forma un triángulo obtuso; si A2 < B2 + C2 entonces forma un triángulo agudo; si
A2 = B2 = C2 entonces forma un triángulo equilátero.
Nombre del archivo 'td20.py'
Desarrollo del algoritmo en código Python
'''

print "\nIngrese los 3 (tres) lados del triángulo para saber de que tipo es."
a = raw_input("\nIngrese el primer valor: ")
a = int(a)
b = raw_input ("\nIngrese el segundo valor: ")
b = int(b)
c = raw_input("\nIngrese el tercer valor: ")
c = int(c)

if a >= b + c:
	print "\nNo es posible formar un triángulo con los valores ingresados."
else:
	if a ** 2 == b ** 2 + c ** 2:
		print "\nLos valores ingresados forman un triángulo-rectángulo."
	else:
		if a ** 2 > b ** 2 == c ** 2:
			"\nLos valores ingresados forman un trángulo obtuso."
		else:
			if a ** 2 < b ** + c ** 2:
				print "\nLos valores ingresados forman un triángulo agudo."
			else:
				if a ** 2 == b ** 2 == c ** 2:
					print "\nLos valores ingresados forman un triángulo-equilatero."

raw_input("\nOprima la trcla ENTER para finalizar.")