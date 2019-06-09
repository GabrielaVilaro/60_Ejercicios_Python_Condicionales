
#coding=UTF-8


'''
Ejercicio: 53, Tema: Toma de desiciones
Enunciado --> (53.)Leer 2 fechas, cada una de ellas representada por tres valores (dd/mm/aaaa) e informar cuál es
anterior.
Nombre del archivo 'td53.py'
Desarrollo del algoritmo en código Python
'''

dia_1 = raw_input("\nIngrese el día 1: ")
dia_1 = int (dia_1)
mes_1 = raw_input("\nIngrese el mes 1: ")
mes_1 = int(mes_1)
anio_1 = raw_input("\nIngrese el año 1: ")
anio_1 = int(anio_1)

print "\nLa primer fecha ingresada es: ", dia_1, mes_1, anio_1

dia_2 = raw_input ("\nIngrese el día 2: ")
dia_2 = int(dia_2)
mes_2 = raw_input ("\nIngrese el mes 2: ")
mes_2 = int(mes_2)
anio_2 = raw_input ("\nIngrese el año 2: ")
anio_2 = int(anio_2)

print "\nLa segunda fecha ingresada es: ", dia_2, mes_2, anio_2

if dia_1 < dia_2:
	menor_dia = dia_1
else:
	menor_dia = dia_2
if mes_1 < mes_2:
	menor_mes = mes_1
else:
	menor_mes = mes_2
if anio_1 < anio_2:
	menor_anio = anio_1
else:
	menor_anio = anio_2
print "\nLa fecha anterior es: ", menor_dia, menor_mes, menor_anio


raw_input("\nOprima ENTER para finalizar.")