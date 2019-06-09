#coding=UTF-8


'''
Ejercicio: 32, Tema: Toma de desiciones
Enunciado --> (32.) Ingresar dos números y multiplicarlos entre si. Informar:
32.1. ¿El resultado es positivo?
32.2. ¿Alguno de los números ingresados es cero?
Nombre del archivo 'td32.py'
Desarrollo del algoritmo en código Python
'''
print "Multiplica 2 números e informa si el resultado es positivo y si uno de los números es 0."
num1 = raw_input("\nIngrese el primer número: ")
num1 = int(num1)
num2 = raw_input("\nIngrese el segundo número: ")
num2 = int(num2)
multiplicacion = num1 * num2
print multiplicacion

if multiplicacion >= 0:
	print"\nEl resultado es positivo"


if num1 == 0 or num2 == 0:
	print "\nUno de los números ingresados es 0 (cero)." 

raw_input("\nOprima la tecla ENTER para finalizar.")
