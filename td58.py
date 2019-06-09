#coding=UTF-8


'''
Ejercicio: 58, Tema: Toma de desiciones
Enunciado --> (58.)Dado el ingreso de 2 números decimales, emitir uno de estos 3 mensajes según corresponda: “El
primero es mayor que el segundo”, “El primero es menor que el segundo” o “Ambos son iguales”.
Nombre del archivo 'td58.py'
Desarrollo del algoritmo en código Python
'''
decimal1 = raw_input("\nIngrese un número decimal: ")
decimal1 = float(decimal1)
decimal2 = raw_input("\nIngrese el segundo” número decimal: ")
decimal2 = float(decimal2)

if decimal1 > decimal2:
	print "\nEl primer decimal ingresado es mayor al segundo."
else:
	if decimal1 < decimal2:
		print "\nEl primer decimal ingresado es menor al segundo."
	else:
		if decimal1 == decimal2:
			print "\nAmbos son iguales."

raw_input("\nOprima la tecla ENTER para finalizar.")