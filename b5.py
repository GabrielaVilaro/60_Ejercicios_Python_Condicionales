#coding=UTF-8

'''
Ejercicio: 5, Tema: Repeticiones, bucles e iteraciones.
Enunciado --> (5.)Modificar el programa anterior de tal forma que el 
resultado de la operación se almacene en una variable y luego se 
muestre el contenido de la misma.
Nombre del archivo 'b5.py'
Desarrollo del algoritmo en código Python
'''
n = raw_input("Ingrese un número: ")
n = int(n)
while n > 0:
	cuadrado = n ** 2
	print "El cuadrado es: ", cuadrado
	break
raw_input("Oprima ENTER para finalizar el programa.")
