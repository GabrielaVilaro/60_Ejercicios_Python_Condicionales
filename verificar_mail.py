#coding=UTF-8


email = False #Comienza siendo falsa la condición

miEmail = raw_input("Introduce tu email: ") #guarda el email ingresado en una variable

for i in miEmail: #Lee caracter por caracter del email ingresado
	
	if i == "@" : #Si dentro de I (miEmail) esta el caracter @ la condicion de email pasa a ser True, verdadera

		email=True

if email == True: #y si la condicion es verdadera debera mostrar el siguiente mensaje:
	
	print "El email es correcto"

else: #en caso de que la condicon sea falsa muestra este otro

	print "El email es incorrecto"
	
raw_input("Oprima ENTER para finalizar.")
