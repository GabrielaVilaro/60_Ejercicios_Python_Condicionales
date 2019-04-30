#coding=UTF-8


'''
Ejercicio: 11, Tema: Toma de desiciones
Enunciado --> (11.) Construir un algoritmo que permita leer dos número enteros y determinar cuál de los dos es el mayor.
Nombre del archivo 'td11.py'
Desarrollo del algoritmo en código Python
'''

num1 = raw_input("\nIngrese el primer número: ")
num1 = int(num1)
num2 = raw_input("\nIngrese el segundo número: ")
num2 = int(num2)
if num1 < num2:
    print"\nEl primer número es MENOR al segundo número ingresado."
else:
    print "\nEl primer número es MAYOR al segundo número ingresado."
raw_input("\nOprima ENTER para salir. ")
