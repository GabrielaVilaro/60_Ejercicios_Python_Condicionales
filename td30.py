#coding=UTF-8


'''
Ejercicio: 30, Tema: Toma de desiciones
Enunciado --> (30.)Ingresar dos números positivos y sumarlos. Validar los datos. Informar:
30.1. ¿Cuántos números impares se ingresaron?
30.2. ¿La suma es múltiplo de 2?
Nombre del archivo 'td30.py'
Desarrollo del algoritmo en código Python
'''
print "\nInforma la cantidad de números impares ingresados y si la suma de los números es múltiplo de 2."

def validar_positivo(n):
    if n < 0:
        print "\nError, debe ingresar solo números positivo."
        n = raw_input("\n\nReingrese el número: ")
        n = int (n)
        n = validar_positivo(n)
    return n

num1 = raw_input("\nIngresar un número positivo: ")
num1 = int(num1)
num1 = validar_positivo(num1)
num2 = raw_input("\nIngresar otro número positivo: " )
num2 = int(num2)
num2 = validar_positivo(num2)

if num1 % 2 != 0 and num2 % 2 != 0:
    print "\nSe han ingresado 2 (dos) números impares."
else:
    if num1 % 2 != 0 or num2 % 2 != 0:
        print "\nSe ha ingresado 1 número impar."

suma = num1 + num2 
print "\nLa suma de los números ingresados es: ", suma
if suma % 2 == 0:
    print "\nEl resultado de la suma: ", suma, "es multiplo de 2."

raw_input("\nOprima la tecla ENTER para finalizar.")

