#coding=UTF-8


'''
Ejercicio: 60, Tema: Toma de desiciones
Enunciado --> (60.)Dado el ingreso de 10 caracteres, contar y mostrar cuantas veces se repite el primer caracter entre los
9 caracteres restantes.
Nombre del archivo 'td60.py'
Desarrollo del algoritmo en código Python
'''
palabra = raw_input("\nIngrese una palabra de 10 carateres: ")

if len (palabra) > 10 or len (palabra) < 10:
    	print "\nNo se puede introducir más o menos de 10 caracteres."
    	palabra = raw_input("\nReingrese la palabra: ")
else:
	pass

c1 = palabra[0]
c2 = palabra[1]
c3 = palabra[2] 
c4 = palabra[3]
c5 = palabra[4]
c6 = palabra[5]
c7 = palabra[6]
c8 = palabra[7]
c9 = palabra[8]
c10 = palabra[9]

p = 0

if c1 == c1:
	p = 1
if c2 == c1:
	p = 1 + p
if c3 == c1:
	p = 1 + p
if c4 == c1:
	p = 1 + p
if c5 == c1:
	p = 1 + p
if c6 == c1:
	p = 1 + p
if c7 == c1:
	p = 1 + p
if c8 == c1:
	p = 1 + p
if c9 == c1:
	p = 1 + p
if c10 == c1:
	p = 1 + p
print "\nLa cantidad de veces que se repite el primer caracter es: ", p

raw_input("\nOprima ENTER para finalizar.")