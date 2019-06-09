#coding=UTF-8


'''
Ejercicio: 56, Tema: Toma de desiciones
Enunciado --> (56.)Dado el ingreso de 10 caracteres, contar y emitir un mensaje con la cantidad de letras “a” que hay
entre los valores ingresados.
Nombre del archivo 'td56.py'
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

if c1 == "a":
	a = 1
if c2 == "a":
	a = 1 + a
if c3 == "a":
	a = 1 + a
if c4 == "a":
	a = 1 + a
if c5 == "a":
	a = 1 + a
if c6 == "a":
	a = 1 + a
if c7 == "a":
	a = 1 + a
if c8 == "a":
	a = 1 + a
if c9 == "a":
	a = 1 + a
if c10 == "a":
	a = 1 + a
print "\nLa cantidad de veces que se repite la letra A es: ", a

raw_input("\nOprima ENTER para finalizar.")