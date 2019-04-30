#coding=UTF-8


'''
Ejercicio: 12, Tema: Toma de desiciones
Enunciado --> (12.) Construir un algoritmo que permita leer un número entero positivo de 2 dígitos y determinar a cuánto es igual la suma de sus dos dígitos.
Nombre del archivo 'td12.py'
Desarrollo del algoritmo en código Python
'''

def validar_numero(num):
    if num < 9 or num > 100:
        if num < 0:
            print "\nEl número ingresado no es de dos dígitos y es negativo."
        else:
            print "\nEl número ingresado no es de dos dígitos."
        print "\n\nError al ingresar el número."
        print "\n\n\nRecuerde que debe ingresar solo números positivos y de dos dígitos."
        num = raw_input("\n\nReingrese el número: ")
        num = int (num)
        num = validar_numero(num)
    return num


print "\n\n\nDebe ingresar solo números positivos y de dos dígitos."
valor = raw_input("\n\nIngrese el número: ")
valor = int (valor)
valor = validar_numero(valor)
unidad = valor % 10
decena = valor / 10
sumados = decena + unidad
print "\nLa suma del valor de dos dígitos ingresados  es: ", sumados
raw_input("\t\n\nOprima la tecla ENTER para salir.")
