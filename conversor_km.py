#coding=UTF-8

#conversor de medidas
 
def conversor():
	print "Bienvenido/a"
	print "Elige opcion en la que quieres que se expresa la cantidad: "
	opcion = raw_input ("Elige opcion < cm, m, km >: ")
	cantidad = raw_input("Ingrese la cantidad:   ")
	cantidad = float(cantidad)
 
	if opcion == 'cm':
		print "Calculando."
		print cantidad / 100, 'metros'
		print cantidad / 1000, 'kilometros'
 
	if opcion == 'm':
		print 'Calculando.'
		print cantidad * 100 ,'centimetros'
		print cantidad / 1000, 'kilometros'
 
	if opcion == 'km':
		print 'Calculando.'
		print cantidad * 1000, 'metros'
		print cantidad * 100000, 'centimetros'
 
conversor()