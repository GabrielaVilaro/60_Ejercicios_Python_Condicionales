#coding=UTF-8


'''
Ejercicio: 61, Tema: Toma de desiciones
Enunciado --> (61.)Ingresar una fecha con el formato DD/MM/AAAA e informar si es válida. Considerar si el año es bisiesto.
Nombre del archivo 'td61.py'
Desarrollo del algoritmo en código Python
'''

from datetime import date

fecha = raw_input("Ingresar fecha en formato DD/MM/AAA: ")
fecha = str.format(fecha, "%d/%m/%y")

dia = fecha[0:2]
dia = int(dia)
mes = fecha[3:5]
mes = int(mes)
anio = fecha[6:10]
anio = int(anio)

if dia <= 0 or dia > 31:
	print "La fecha no es válida, revise el día."

if mes <= 0 or mes > 12:
	print "La fecha no es válida, revise el mes."

if anio <= 0 or anio > 2018:
	print "La fecha no es válida, revise el año."

raw_input ("Oprima la tecla ENTER para finalizar.")