#coding=UTF-8

def generaPares(limite):

	num = 1

	miLista = []

	while num < limite:

		miLista.append(num * 2)

		num = num + 1

	return miLista

print generaPares(10)

raw_input("Oprima ENTER para finalizar el programa.")