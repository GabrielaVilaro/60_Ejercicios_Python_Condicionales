#coding=UTF-8

""" UdemyBucles: Ejercicio N°9 - Escribe un programa que dados dos números,
uno real (base) y un entero positivo (exponente), saque por pantalla el 
resultado de la potencia. No se puede utilizar el operador de potencia."""

base = raw_input("Ingrese una base: ")
base = int(base)

exponente = raw_input("Ingrese un exponente: ")
exponente = int(exponente)

potencia = 1

while exponente > 0:
	potencia = potencia * base
	exponente = exponente - 1

print "La potencia del número ingresado es: ", potencia

raw_input("Oprima la tecla ENTER para finalizar el programa.")