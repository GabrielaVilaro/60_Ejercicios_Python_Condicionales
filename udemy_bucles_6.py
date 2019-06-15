#coding=UTF-8

""" UdemyBucles: Ejercicio N°6 - Escribir un programa que imprima todos 
los números pares entre dos números que se le pidan al usuario."""

num1 = raw_input("Ingrese un número: ")
num1 = int(num1)
num2 = raw_input("Ingrese otro número: ")
num2 = int(num2)

for i in range(num1, num2):
	if i % 2 != 0:
		print "Los números pares entre los dos que ingresaste son: ", i + 1
		
raw_input("Oprima ENTER para finalizar el programa.")