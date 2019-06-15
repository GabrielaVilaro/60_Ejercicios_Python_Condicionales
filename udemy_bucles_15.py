#coding=UTF-8

""" UdemyBucles: Ejercicio N°15 - Una persona adquirió un producto para 
pagar en 20 meses. El primer mes pagó 10 $, el segundo 20 $, el tercero 
40 $ y así sucesivamente. Realizar un algoritmo para determinar cuánto 
debe pagar mensualmente y el total de lo que pagó después de los 20 meses."""

pago_total = 0
pago = 10

for mes in range(1, 21):
	pago_total = pago_total + pago
	pago = pago * 2 #de dos en dos

print "Por mes paga: ", pago
print "En total pagó: ", pago_total

raw_input("Presione ENTER para finalizar el programa.")