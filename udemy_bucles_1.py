#coding=UTF-8

""" UdemyBucles: Ejercicio N°1 - Crea una aplicación que pida un número y 
calcule su factorial(El factorial de un número es el producto de todos 
los enteros entre 1 y el propio número y se representa por el número 
seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120)"""

num = raw_input("Ingrese un número: ")
num = int(num)

resultado = 1

for i in range(1, num+1):
	resultado = resultado * i
print "El resultado es",  resultado

raw_input("Presione ENTER para finalizar el programa.")