#coding=UTF-8


'''
Ejercicio: 6, Tema: Toma de desiciones
Enunciado --> (6.) Se ingresa al proceso 2 números enteros y un código de operación, (1=Suma, 2=Multiplicación,
3=Diferencia). Se desea obtener el resultado de la operación realizada y un texto que declare cuál fue
esa operación.
Nombre del archivo 'td6.py'
Desarrollo del algoritmo en código Python
'''

print "\nDebe ingresar dos números enteros"
num1 = raw_input ("\nIngrese el primer número: ")
num1 = int(num1)
num2 = raw_input ("\nIngrese el segundo número: ")
num2 = int(num2)
print "\nSi desea obtener la SUMA de los números ingrese un 1 "
print "\nSi desea obtener la MULTIPLICACIÓN de los números ingrese un 2 "
print "\nSi desea obtener la DIFERENCIA de los números ingrese un 3"
operacion = raw_input("\nIngrese la operación que desea realizar: ")
operacion = int(operacion)

if operacion == 1:
	print num1 + num2, "\nLa operación realizada fue una SUMA."
	
else:
	if operacion == 2:
		print num1 * num2, "\nLa operación realizada fue una MULTIPLICACIÓN."
	else:
		if operacion == 3:
			print num1 % num2, "\nLa operación realizada fue una DIFERENCIA."

raw_input("\nOprima la tecla ENTER para finalizar.")