#coding=UTF-8

#Ejercicio de "Píldoras Informáticas."

def main ():
	print "Convierte medidas inglesas a sistema métrico"
	millas = raw_input("¿Cuántas millas?: ")
	millas = float(millas)
	pies = raw_input("¿Cuántos pies?: " )
	pies = float(pies)
	pulgadas = raw_input("¿Cuántas pulgadas?: ")
	pulgadas = float(pulgadas)

	metros = 1609.344 * millas + 0.3048 * pies + 0.0254 * pulgadas
	print "La longitud es de ", metros, "metros"

main()