#coding=UTF-8


'''
Ejercicio: 59, Tema: Toma de desiciones
Enunciado --> (59.)Se leen 3 valores numéricos. Si el primer valor es mayor que el segundo; pero menor que el tercero, se
deberá mostrar el producto de los 3 valores. Caso contrario, se deberá emitir la suma de los 3 valores.
Nombre del archivo 'td59.py'
Desarrollo del algoritmo en código Python
'''
num1 = raw_input("\nIngrese el primer número: ")
num1 = int(num1)
num2 = raw_input("\nIngrese el segundo número: ")
num2 = int(num2)
num3 = raw_input("\nIngrese el tercer número: ")
num3 = int(num3)

producto = num1 * num2 * num3

suma = num1 + num2 + num3

if num1 > num2 and num1 < num3:
	print "\nEl producto de los 3 valores ingresado es: ", producto
else:
	print "\nLa suma de los 3 valores ingresados es: ", suma

raw_input("\nOprima ENTER para finalizar.")