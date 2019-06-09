#coding=UTF-8


'''
Ejercicio: 28, Tema: Toma de desiciones
Enunciado --> (28.) Imprimir tres números en forma descendente, sin hacer intercambios de valores.
Nombre del archivo 'td28.py'
Desarrollo del algoritmo en código Python
'''
print "\nImprime 3 números en forma descendente"

num1 = raw_input("\nIngrese el primer número: ")
num1 = int(num1)
num2 = raw_input("\nIngrese el segundo número: ")
num2 = int(num2)
num3 = raw_input("\nIngrese el tercer número: ")
num3 = int(num3)

if num1 > num2 and num2 > num3:
	print num1, num2, num3
else:
	if num1 < num2 and num2 < num3:
		print num3, num2, num1
	else:
		if num2 > num3 and num1 > num3:
			print num2, num1, num3
		else:
			if num2 > num1 and num2 > num3:
				print num2, num3, num1
			else:
				if num1 < num3 and num2 < num3:
					print num3, num1, num2
				else:
					if num1 > num2 and num2 < num3:
						print num1, num3, num2

raw_input("\nPresione la tecla ENTER para finalizar.")