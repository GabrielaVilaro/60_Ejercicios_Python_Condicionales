#coding=UTF-8

""" UdemyBucles: Ejercicio N°14 - Una persona se encuentra en el kilómetro
70 de una carretera, otra se encuentra en el km 150, los coches tienen 
sentido opuesto y tienen la misma velocidad. Realizar un programa para 
determinar en qué kilómetro de esa carretera se encontrarán."""

kilometro1 = 70
kilometro2 = 150

while kilometro1 != kilometro2:
	kilometro1 = kilometro1 + 1
	kilometro2 = kilometro2 -1
print "Se encontrarán en el kilómetro: ", kilometro1

raw_input("Oprima ENTER para finalizar el programa.")