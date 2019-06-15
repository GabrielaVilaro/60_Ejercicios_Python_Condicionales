#coding=UTF-8

""" UdemyBucles: Ejercicio N°10 - Algoritmo que muestre la tabla de 
multiplicar de los números 1,2,3,4 y 5."""


for tabla in range(1, 6):
	for num in range(1, 11):
		producto = num * tabla
		print tabla, "x", num, "=", producto
		
print "Esas fueron las tablas del 1 al 5."
	
raw_input("Oprima ENTER para finalizar.")