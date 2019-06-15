#coding=UTF-8

'''
Ejercicio: 4, Tema: Repeticiones, bucles e iteraciones.
Enunciado --> (4.) Realizar un programa que solicite un número entero por 
teclado y muestre por pantalla el cuadrado del mismo.
Nombre del archivo 'b4.py'
Desarrollo del algoritmo en código Python
'''

n = raw_input("Ingrese un número: ")
n = int(n)
while n > 0:
	print "El cuadrado es: ", n ** 2
	break
raw_input("Oprima ENTER para finalizar el programa.")