#coding=UTF-8


'''
Ejercicio: 7, Tema: Toma de desiciones
Enunciado --> (7.) Se ha determinado que luego del uso del programa el operador es falible. Mantener el programa del
ejercicio anterior, tal que muestre un mensaje de error en el caso de que el código de operación se
encuentre fuera del rango.
Nombre del archivo 'td7.py'
Desarrollo del algoritmo en código Python
'''

print "\nDebe ingresar dos números enteros"

num1 = raw_input ("\nIngrese el primer número: ")
num1 = int(num1)
num2 = raw_input ("\nIngrese el segundo número: ")
num2 = int(num2)

print "\nSi desea obtener la suma de los números ingrese un 1 "
print "\nSi desea obtener la multiplicación de los números ingrese un 2 "
print "\nSi desea obtener la diferencia de los números ingrese un 3"

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
		else:
			if operacion >=4:
				print "\nError al ingresar el código de operación."

raw_input("\nOprima la tecla ENTER para finalizar.")
