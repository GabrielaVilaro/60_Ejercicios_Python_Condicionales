
#coding=UTF-8


'''
Ejercicio: 52, Tema: Toma de desiciones
Enunciado --> (52.)Desarrollar un algoritmo que lea los valores de la temperatura del día anterior durante la mañana,
tarde y noche; y que las informe en orden creciente.
Nombre del archivo 'td52.py'
Desarrollo del algoritmo en código Python
'''

temp_manana = raw_input ("\nIngrese la temperatura del día de ayer por la mañana: ")
temp_manana = int(temp_manana)
temp_tarde = raw_input("\nIngrese la temperatura del día de ayer por la tarde: ")
temp_tarde = int(temp_tarde)
temp_noche = raw_input("\nIngrese la temperatura del día de ayer por la noche: ")
temp_noche = int(temp_noche)

if temp_manana < temp_tarde and temp_tarde < temp_noche:
	print temp_manana, temp_tarde, temp_noche
else:
	if temp_manana > temp_tarde and temp_tarde > temp_noche:
		print temp_noche, temp_tarde, temp_manana
	else:
		if temp_tarde < temp_noche and temp_manana < temp_noche:
			print temp_tarde, temp_manana, temp_noche
		else:
			if temp_tarde < temp_manana and temp_tarde < temp_noche:
				print temp_tarde, temp_noche, temp_manana
			else:
				if temp_manana > temp_noche and temp_tarde > temp_noche:
					print temp_noche, temp_manana, temp_tarde
				else:
					if temp_manana < temp_tarde and temp_tarde > temp_noche:
						print temp_manana, temp_noche, temp_tarde

raw_input("\nPresione la tecla ENTER para finalizar.")