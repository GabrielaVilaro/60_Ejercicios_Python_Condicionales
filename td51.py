
#coding=UTF-8


'''
Ejercicio: 51, Tema: Toma de desiciones
Enunciado --> (51.) Un postulante a un empleo realizó un test de capacitación. Se deberán leer la cantidad de preguntas
formuladas y la cantidad de respuestas correctas. Informar el nivel del postulante según el porcentaje
de respuestas correctas obtenidas.
51.1. Nivel SUPERIOR: mayor o igual a 90%.
51.2. Nivel MEDIO: mayor o igual a 75% y menor 90%.
51.3. Nivel REGULAR: mayor o igual a 50% y menor a 75%.
51.4. Fuera de Nivel: restantes casos.
Nombre del archivo 'td51.py'
Desarrollo del algoritmo en código Python
'''

cant_preguntas = raw_input("\nIngrese la cantidad de preguntas formuladas al postulante: ")
cant_preguntas = float(cant_preguntas)
resp_correctas = raw_input("\nIngrese la cantidad de respuestas correctas: ")
resp_correctas = float(resp_correctas)

def porcentaje (parte, todo):
	return parte / todo * 100

porc_resp = porcentaje (resp_correctas, cant_preguntas)
porc_resp = int(porc_resp)

if porc_resp >= 90:
	print "\nEl nivel del postulante es SUPERIOR."
else:
	if porc_resp >= 75 and porc_resp < 90:
		print "\nEl nivel del postulante es MEDIO."
	else:
		if porc_resp >= 50 and porc_resp < 75:
			print "\nEl nivel del postulante es REGULAR."
		else:
			if porc_resp <= 49:
				print "\nEl postulante se encuentra FUERA DE NIVEL."

raw_input ("\nOprima la tecla ENTER para finalizar.")