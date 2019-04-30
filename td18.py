#coding=UTF-8


'''
Ejercicio: 18, Tema: Toma de desiciones
Enunciado --> (18.) Construir un algoritmo que permita leer un número entero positivo de un dígito y determinar si ese
número es un número primo.
Nombre del archivo 'td18.py'
Desarrollo del algoritmo en código Python
'''

def validar_num(num):
    if num > 9 or num < 0:
        print "\nEl número ingresado no es de un dígito o es negativo."
        print "\nRecuerde que debe inhresar un número positivo de un dígito."
        num = raw_input("\n\nReingrese el número: ")
        num = int(num)
        num = validar_num(num)
    else:
        if num == 2 or num == 3 or num == 5 or num == 7:
            print "\nEl número ingresado es primo"
            raw_input("Oprima ENTER para finalizar.")
        else:
            print "\nEl número ingresado NO es primo."
            raw_input("Oprima ENTER para finalizar.")
    return num
      
print "\nDebe ingresar un número positivo de un dígito."
valor = raw_input ("\nIngrese el número: ")
valor = int(valor)
valor = validar_num(valor)
