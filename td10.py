#coding=UTF-8


'''
Ejercicio: 10, Tema: Toma de desiciones
Enunciado --> (10.) Construir un algoritmo que permita leer dos números enteros y determinar si son iguales.
Desarrollo del algoritmo en código Python
'''

num1 = raw_input("\nIngrese un número: ")
num1 = int(num1)
num2 = raw_input("\nIngrese otro número: ")
num2 = int(num2)
if num1 == num2:
    print"\nLos números ingresados son iguales"
else:
    print"\nLos números ingresados son difertentes."
raw_input("\nOprima ENTER para salir.")
