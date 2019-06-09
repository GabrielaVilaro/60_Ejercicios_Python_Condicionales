#coding=UTF-8


'''
Ejercicio: 43, Tema: Toma de desiciones
Enunciado --> (43.) Ingresar dos números, calcular e informar:
43.1. La suma, si el primero es menor que el segundo.
43.2. La diferencia, si el primero es mayor que el segundo.
43.3. El producto, si son iguales.
Nombre del archivo 'td43.py'
Desarrollo del algoritmo en código Python
'''

num1 = raw_input("\nIngrese el primer número: ")
num1 = int(num1)
num2 = raw_input("\nIngrese el segundo número: ")
num2 = int(num2)

if num1 < num2:
	print "\nLa suma de los números es de: ", num1 + num2
else:
	if num1 > num2:
		print "\nLa diferencia entre los números es de: ", num1 % num2
	else:
		if num1 == num2:
			print "\nEl producto de los dos números es de: ", num1 * num2

raw_input("\nOprima ENTER para finalizar.")