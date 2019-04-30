#coding=UTF-8


'''
Ejercicio: 16, Tema: Toma de desiciones
Enunciado --> (16.) Construir un algoritmo que permita leer un número entero de tres dígitos y determinar si el primer
dígito es múltiplo de los otros dos.
Nombre del archivo 'td16.py'
Desarrollo del algoritmo en código Python
'''

def validar_num (num):
	if num > 99 and num < 999:
		return num
	else:
		print "\nError, debe ingresar un número de 3 (tres) dígitos"
		num = raw_input("\n\nReingrese el número: ")
        num = int (num)
    	num = validar_num(num)

print "\nDeebe ingresar un número de 3 (tres) dígitos."

valor = raw_input("\nIngrese el número: ")
valor = int (valor)
valor = validar_num(valor)

dig1 = valor / 10 / 10
dig2 = valor / 10 % 10
dig3 = valor % 10

if dig1 % dig2 == 0:
    print "\nEl primer dígito: ", dig1 , "es múltiplo del segundo: ", dig2
else:
    if dig1 % dig3 == 0:
        print "\nEl primer dígito: ", dig1 , "es múltiplo del tercero: ", dig3
    else:
        if dig1 % dig2 == 0 and dig1 % dig3 == 0:
            print "\nEl primer dígito: ", dig1, "es múltiplo del segundo: ", dig2, "y el tercero: ", dig3
        else:
            print "\nEl primer dígito: " , dig1, "NO es múltiplo del segundo: ", dig2 , "ni del tercero: ", dig3
raw_input ("\nOprima ENTER para finalizar.")

  






