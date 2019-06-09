#coding=UTF-8


'''
Ejercicio: 45, Tema: Toma de desiciones
Enunciado --> (45.) Ingresar 4 números, hallar el promedio, e informar cuántos son mayores que el promedio.
Nombre del archivo 'td45.py'
Desarrollo del algoritmo en código Python
'''

num1 = raw_input("\nIngrese el primer número: ")
num1 = int(num1)
num2 = raw_input("\nIngrese el segundo número: ")
num2 = int(num2) 
num3 = raw_input("\nIngrese el tercer número: ")
num3 = int(num3)
num4 = raw_input("\nIngrese el cuarto número: ")
num4 = int(num4)

promedio = (num1 + num2 + num3 + num4) / 4

print "\nEl promedio obtenido de los números ingresados es: ", promedio

if num1 > promedio:
	print "\nEl primer número ingresado es mayor al promedio: ", num1
if num2 > promedio:
	print "\nEl segundo número ingresado es mayor al promedio: ", num2
if num3 > promedio:
	print "\nEl tercer número ingresado es mayor al promedio: ", num3
if num4 > promedio:
	print "\nEl cuarto número ingresado es mayor al promedio: ", num4

				
raw_input("\nOprima la tecla ENTER para finalizar.")



