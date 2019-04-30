#coding=UTF-8


'''
Ejercicio: 17, Tema: Toma de desiciones
Enunciado --> (17.) Construir un algoritmo que permita leer dos números enteros y determinar si uno es múltiplo del
otro.
Nombre del archivo 'td17.py'
Desarrollo del algoritmo en código Python
'''

print "\nDebe ingresar 2 (dos) números enteros."
num1 = raw_input ("\nIngrese el primer número: ")
num1 = int(num1)
num2 = raw_input ("\nIngrese el segundo número: ")
num2 = int(num2)

if num1 % num2 == 0:
    print "\nEl primer número ingresado: ", num1, "es múltiplo del segundo: ", num2
else:
    print "\nEl primer número ingresado: ", num1, "NO es multiplo del segundo: ", num2
raw_input ("Oprima la tecla ENTER para finalizar.")