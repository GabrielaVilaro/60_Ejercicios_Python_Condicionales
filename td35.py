#coding=UTF-8


'''
Ejercicio: 35, Tema: Toma de desiciones
Enunciado --> (35.)Un negocio comercializa un artículo cuyo precio es de $ 3.00 y de acuerdo a la cantidad vendida
efectúa diferentes descuentos:
35.1. Si 0 < cantidad_vendida <= 10 no se hace descuento.
35.2. Si 11 <= cantidad_vendida < 20 se hace un 2% de descuento.
35.3. Si cantidad_vendida > 19 se hace un 4% de descuento
Nombre del archivo 'td35.py'
Desarrollo del algoritmo en código Python
'''
def descuento_porcentaje(parte, todo):
    return parte * todo / 100


cantidad_vendida = raw_input("\nIngrese la cantidad vendida para saber el descuento que corresponde: ")
cantidad_vendida = float(cantidad_vendida)

precio = 3

producto_cantidad = cantidad_vendida * precio

if cantidad_vendida > 0 and cantidad_vendida <= 10:
	print "\nLa cantidad comprada es insuficiente para obtener un descuento."
else:
	if cantidad_vendida >= 11 and cantidad_vendida < 20:
		print "\nEl descuento aplicado es de un %2: ", descuento_porcentaje(2, producto_cantidad)
	else:
		if cantidad_vendida > 19:
			print "\nEl descuento aplicado es de un %4: ", descuento_porcentaje(4, producto_cantidad)

raw_input("\nOprima la tecla ENTER para finalizar.")

