#coding=UTF-8


'''
Ejercicio: 22, Tema: Toma de desiciones
Enunciado --> (22.) Simular una tirada de dados y ver si se produce generala. Realizarlo de dos formas:
22.1. Comparando los dados de a dos.
22.2. Comparando los cinco dados simultáneamente.
Nombre del archivo 'td22.py'
Desarrollo del algoritmo en código Python
'''
print "\nSimulador de generala ¡Juego al azar!."
raw_input("\nPresione ENTER para realizar la tirada.")
import random

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)
d4 = random.randint(1, 6)
d5 = random.randint(1, 6)

if d1 == d2 == d3 == d4 == d5:
	print "\n¡Generala!"
else:
	if d1 == d2 and d2 == d3 and d3 == d4 and d4 == d5:
		print "\n!Generala!"
	else:
		print "\nEl resultado del dado 1 fue: ", d1
		print "\nEl resultado del dado 2 fue: ", d2
		print "\nEl resultado del dado 3 fue: ", d3
		print "\nEl resultado del dado 4 fue: ", d4
		print "\nEl resultado del dado 5 fue: ", d5
raw_input("\nPresione la tecla ENTER para finalizar.")


