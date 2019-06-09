#coding=UTF-8


'''
Ejercicio: 46, Tema: Toma de desiciones
Enunciado --> (46.) Un artículo se vende en distintos supermercados a diferentes precios, estos son: P1 en el
supermercado A, P2 en el supermercado B, y P3 en el supermercado C. Informar:
46.1. ¿Cuál es el precio promedio del artículo?
46.2. ¿Qué supermercado vende más barato?
46.3. ¿En qué porcentaje resulta más caro el artículo respecto de los otros dos supermercados?
Nombre del archivo 'td46.py'
Desarrollo del algoritmo en código Python
'''

super_a = raw_input("\nIngrese el precio del producto del supermercado A: ")
super_a = float(super_a)
super_b = raw_input("\nIngrese el precio del producto del supermercado B: ")
super_b = float(super_b)
super_c = raw_input("\nIngrese el precio del producto del supermercado C: ")
super_c = float(super_c)

total = super_a + super_b + super_c

def porcentaje(parte, todo):
	return parte / todo * 100

print "\nEl promedio del valor del producto es de: ", total / 3

if super_a < super_b and super_a < super_c:
	menor = super_a
	print "\nEl supermercado que tiene el menor precio es el: A"
	print "\nEs un %", porcentaje(super_b, total), "Más barato que el B."
	print "\nEs un %", porcentaje(super_c, total),"Más barato que el C."
else:
	if super_b < super_a and super_b < super_c:
		menor = super_b
		print "\nEl supermercado que tiene el menor precio es el: B"
		print "\nEs un %", porcentaje(super_a, total), "Más barato que el B."
		print "\nEs un %", porcentaje(super_c, total),"Más barato que el C."
	else:
		if super_c < super_a and super_c < super_b:
			menor = super_c
			print "\nEl supermercado que tiene el menor precio es el: C"
			print "\nEs un %", porcentaje(super_a, total), "Más barato que el B."
			print "\nEs un %", porcentaje(super_b, total),"Más barato que el C."

raw_input("\nOprima la tecla ENTER para finalizar.")







