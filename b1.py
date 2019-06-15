#coding=UTF-8


'''
Ejercicio: 1, Tema: Repeticiones, bucles e iteraciones.
Enunciado --> (1.) Se ha determinado que es poco funcional que el programa culmine cuando el operador comete un
error en el ingreso del código de operación. Mantener el programa del ejercicio 7 de Toma de decisión
de tal forma que vuelva a solicitar el código de operación en caso de error.
Nombre del archivo 'b1.py'
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

while operacion >= 4:
	print "Invalido."
	operacion = raw_input ("Reingrese: ")
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