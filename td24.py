#coding=UTF-8


'''
Ejercicio: 24, Tema: Toma de desiciones
Enunciado --> (24.) Se ingresan 5 valores A, B, C, D, E y un código. Informar según sea el código:
24.1. Código=1 Informar A + B + C + D + E
24.2. Código=2 Informar A + B + C + D – E
24.3. Código=3 Informar A + B
No habrá otros códigos.
Nombre del archivo 'td24.py'
Desarrollo del algoritmo en código Python
'''
print "Se ingresan 5 números y se informa según el código ingresado."
a = raw_input("\nIngrese un número: ")
a = int(a)
b = raw_input("\nIngrese un número: ")
b = int(b)
c = raw_input("\nIngrese un número: ")
c = int(c)
d = raw_input("\nIngrese un número: ")
d = int(d)
e = raw_input("\nIngrese un número: ")
e = int(e)

codigo = raw_input("\nIngrese un código, puede ser 1, 2 o 3: ")
codigo = int(codigo)

if codigo == 1:
	print a + b + c + d + e
else:
	if codigo == 2:
		print a + b + c + d - e
	else:
		if codigo == 3:
			print a + b
		else:
			if codigo >=4 or codigo < 0:
				print "\nEl código ingresado NO es válido."

raw_input("\nOprima ENTER para finalizar.")