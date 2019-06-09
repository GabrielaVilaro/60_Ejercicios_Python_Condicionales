#coding=UTF-8


'''
Ejercicio: 29, Tema: Toma de desiciones
Enunciado --> (29.) Una organización comercial compra directamente de fábrica, y de acuerdo a la cantidad comprada
recibe diferentes bonificaciones.
29.1. Si cant_comprada <= 1000 unidades Bonificación: 5 unidades.
29.2. Si 1000 < cant_comprada < 1501 unidades Bonificación: 2% de unidades.
29.3. Si 1500 < cant_comprada <= 2000 unidades Bonificación: 3% de unidades.
29.4. Si cant_comprada > 2000 unidades Bonificación: 100 unidades.
Informar: La cantidad de unidades que recibe en total.
Nombre del archivo 'td29.py'
Desarrollo del algoritmo en código Python
'''
cant_comprada = raw_input("\nIngrese la cantidad de unidades compradas: ")
cant_comprada = int(cant_comprada)

def bonificacion(parte, todo):
    return parte * todo / 100

if cant_comprada <= 1000:
	print "\nLa cantidad de unidades recibidas son: ", cant_comprada + 5
else:
	if cant_comprada > 1000 and cant_comprada <= 1500:
		print "\nLa cantidad de unidades recibidas son: ", cant_comprada + bonificacion(2, cant_comprada)
	else:
		if cant_comprada > 1500 and cant_comprada <= 2000:
			print "\nLa cantidad de unidades recibidas son: ", cant_comprada + bonificacion(3, cant_comprada)
		else:
			if cant_comprada > 2000:
				print "\nLa cantidad de unidades recibidas: ", cant_comprada + 100

raw_input("\nPresione la tecla ENTER para finalizar.")
