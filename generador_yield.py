#coding=UTF-8

#Ejercicio de "Píldoras informáticas."


def generaPares(limite):

	num = 1

	while num < limite: #mientras num 1 sea menor a limite

		yield num * 2 #yield parecido a return, se usa para generar

		num = num + 1

devuelvePares = generaPares(10)

for i in devuelvePares:

	print i

raw_input("Oprima ENTER para finalizar.")
