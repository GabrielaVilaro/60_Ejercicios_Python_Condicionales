#coding=UTF-8

#cajero automático para practicar
import sys #terminar un programa 

clave = 6424
usuario = "GabrielaVilaro"
saldo = 25000
limite_ex = 5000


def extraer_dinero(x, y): #extracciones
	return x - y

def deposita_dinero(x, y): #depositos
	return x + y

print "Bienvenido/a al cajero automático."

contrasena = raw_input("\nIngrese su contraseña: ")
contrasena = int(contrasena)

intentos_c = 0 #intentos de la clave
intentos_n = 0 #intentos del nombre

while contrasena > 0:
	if contrasena != clave:
		print "\nError al ingresar la contraseña."
		contrasena = raw_input("\nReingrese su contraseña: ")
		contrasena = int(contrasena)
		intentos_c = intentos_c + 1
		if intentos_c > 1:
			print "\nYa no puede volver a ingresar su contraseña, agotó los 3 (tres) intentos, comuníquese al 0800-000-000."
			print "\nGracias por utilizar el cajero. Que tenga buenos días."
			sys.exit() #funcion para terminar un programa
	else:
		break

nombre_usuario = raw_input("\nIngrese su nombre de usuario: ")

while nombre_usuario != " ":
	if nombre_usuario != usuario:
		print "\nError al ingresar su nombre de usuario."
		nombre_usuario = raw_input("\nReingrese su nombre de usuario, recuerde respetar mayúsculas: ")
		intentos_n = intentos_n + 1
		if intentos_n > 1:
			print "\nYa no puede volver a ingresar su usuario, agotó los 3 (tres) intentos, comuníquese al 0800-000-000."
			print "\nGracias por utilizar el cajero. Que tenga buenos días."
			sys.exit() #funcion para terminar un programa
	else:
		break

print "\nHas accedido con éxito, Bienvenido/a: ", nombre_usuario
print "\nMenú: "
print "\n1- Consultar saldo."
print "\n2- Extracciones."
print "\n3- Depósito."
print "\n4- Cambiar límite de extracción."
print "\n5- Cambiar contraseña."

opcion = raw_input("\nIngrese el número de la opción que requiera (1, 2, 3, 4, 5): ")
opcion = int(opcion)

while opcion > 0:
	if opcion < 0 or opcion > 5:
		print "Error al ingresar la opción."
		print "La opción ingresada no existe."
		opcion = raw_input("Reingrese el número de opción: ")
		opcion = int(opcion)
	else:
		break

if opcion == 1:
	print "\nUsted eligió la opción CONSULTAR SALDO."
	print "\nSu saldo actual es: $", saldo
	seguir = raw_input("\n¿Desea hacer otra consulta? S/N: ") #mayúsculas
	if seguir == "S":
		opcion = raw_input("\nIngrese el número de la opción que requiera (1, 2, 3, 4, 5): ")
		opcion = int(opcion)
		if opcion == 2:
			print "\nUsted eligió la opción EXTRACCIONES."
			extraer = raw_input("\nIngrese el monto a extraer: ")
			extraer = int(extraer)
			while extraer > 0:
				if extraer > limite_ex:
					print "\nEl monto ingresado excede su límite de extracción."
					extraer = raw_input("\nReingrese el monto a extraer: ")
					extraer = int(extraer)
				else:
					print "\nUsted extrajo $", extraer, "de su saldo."
					print "\nSu saldo actual es: $", extraer_dinero(saldo, extraer)
					saldo_actual = extraer_dinero(saldo, extraer)
					saldo = saldo_actual
					seguir = raw_input("\n¿Desea hacer otra consulta? S/N: ") #mayúsculas
					if seguir == "S":
						opcion = raw_input("\nIngrese el número de la opción que requiera (1, 2, 3, 4, 5): ")
						opcion = int(opcion)
						if opcion == 3:
							print "\nUsted eligió la opcion DEPÓSITO."
							deposito = raw_input("\nIngrese la cantidad de dinero que desea depositar: ")
							deposito = int(deposito)
							while  deposito > 0:
								if deposito < 1:
									print "\nIngrese una cantidad positiva de dinero."
									deposito = raw_input("\nReingrese la cantidad de dinero a depositar: ")
									deposito = int(deposito)
								else:
									print "\nUsted depositó $", deposito, "."
									print "\nSu saldo actual es: ", deposita_dinero(saldo_actual, deposito)

									seguir = raw_input("\n¿Desea hacer otra consulta? S/N: ") #mayúsculas
									if seguir == "S":
										opcion = raw_input("\nIngrese el número de la opción que requiera (1, 2, 3, 4, 5): ")
										opcion = int(opcion)
										if opcion == 4:
											print "\nUsted eligió CAMBIAR LÍMITE DE EXTRACCIÓN."
											cambio_lim = raw_input("\nIngrese el nuevo límite: ")
											cambio_lim = int(cambio_lim)
											print "\nSu límite anterior de", limite_ex, "ahora es de: ", cambio_lim
											limite_ex = cambio_lim
											seguir = raw_input("\n¿Desea hacer otra consulta? S/N: ") #mayúsculas
											if seguir == "S":
												opcion = raw_input("\nIngrese el número de la opción que requiera (1, 2, 3, 4, 5): ")
												opcion = int(opcion)
												if opcion == 5:
													print "\nUsted eligió CAMBIO DE CONTRASEÑA."
													verifica = raw_input("\nIngrese su contraseña anterior: ")
													verifica = int(verifica)
													while verifica != clave:
	 													print "\nContraseña antigua incorrecta."
	 													verifica = raw_input("\nReingrese su contraseña anterior: ")
	 													verifica = int(verifica)
														if verifica == clave:
															clave_nueva = raw_input("\nIngrese su clave nueva: ")
															print "\nSu nueva clave ha sido generada."
															seguir = raw_input("\n¿Desea hacer otra consulta? S/N: ") #mayúsculas
															if seguir == "S":
																opcion = raw_input("\nIngrese el número de la opción que requiera (1, 2, 3, 4, 5): ")
																opcion = int(opcion)
															else:
																print "\nGracias por utilizar el cajero. Que tenga un buen día."
																sys.exit()	
									else:
										print "\nGracias por utilizar el cajero. Que tenga un buen día."
										sys.exit()

					else:
						print "\nGracias por utilizar el cajero. Que tenga un buen día."
						sys.exit()
	else:
		print "\nGracias por utilizar el cajero. Que tenga un buen día."
		sys.exit()