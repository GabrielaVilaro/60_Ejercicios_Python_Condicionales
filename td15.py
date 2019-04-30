#coding=UTF-8


'''
Ejercicio: 15, Tema: Toma de desiciones
Enunciado --> (15.) Construir un algoritmo que permita leer un número entero de dos dígitos y determinar si sus dos
dígitos son iguales.
Nombre del archivo 'td15.py'
Desarrollo del algoritmo en código Python
'''
def validar_numero(num):
    if num < 9 or num > 99:
        print "\nEl número ingresado NO es de dos dígitos."
        print "\n\nError al ingresar el número."
        print "\n\n\nRecuerde que debe ingresar solo números de dos dígitos."
        num = raw_input("\n\nReingrese el número: ")
        num = int(num)
        num = validar_numero(num)
    else:
    	if num / 10 == num % 10: #digito1 = num / 10 - digito2 = num % 10
		print "\nLos digitos del número ingresado son iguales."
	else:
		print "\nLos dígitos del número ingresado son diferentes"
	return num

print "\nDebe ingresar un número entero de 2 (dos) dígitos."
valor = raw_input ("\nIngres el número: ")
valor = int(valor)
valor = validar_numero (valor)
raw_input ("\nOprima la tecla ENTER para finalizar.")





