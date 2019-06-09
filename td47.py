#coding=UTF-8


'''
Ejercicio: 47, Tema: Toma de desiciones
Enunciado --> (47.)Dado el ingreso de 4 valores numéricos, mostrar solo aquellos que resulten superiores al primer valor
ingresado.
Nombre del archivo 'td47.py'
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

if num2 > num1:
    print "\nMayor al primero ingresado: ", num2
if num3 > num1:
    print "\nMayor al primero ingresado: ", num3
if num4 > num1:
    print "\nMayor al primero ingresado: ", num4

raw_input("\nOprima la tecla ENTER para finalizar.")

