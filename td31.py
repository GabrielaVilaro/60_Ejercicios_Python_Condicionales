#coding=UTF-8


'''
Ejercicio: 31, Tema: Toma de desiciones
Enunciado --> (31.)Ingresar tres números mayores a cero. Validar los datos. Multiplicarlos entre si. Informar:
31.1. ¿El resultado es múltiplo de 3?
31.2. ¿Cuántos números pares se ingresaron?
Nombre del archivo 'td31.py'
Desarrollo del algoritmo en código Python
'''
def validar_positivos(n):
	if n < 0:
		print "\nError, Recuerde que debe ingresar solo números mayores a cero."
		n = raw_input("\nReingrese el número: ")
		n = int(n)
		n = validar_positivos(n)
	return n

print "\nDebe ingresar 3 (tres) números mayores a cero para obtener su multiplicación."

num1 = raw_input("\nIngrese el primer número: ")
num1 = int(num1)
num1 = validar_positivos(num1)
num2 = raw_input("\nIngrese el segundo número: ")
num2 = int(num2)
num2 = validar_positivos(num2)
num3 = raw_input("\nIngrese el tercer número: ")
num3 = int(num3)
num3 = validar_positivos(num3)

if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0:
	print "\nSe ingresaron 3 números pares."
else:
	if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 != 0:
		print "\nSe ingresaron 2 números pares."
	else:
		if num1 % 2 == 0 and num2 % 2 != 0 and num3 % 2 == 0:
			print "\nSe ingresaron 2 números pares."
		else:
			if num1 % 2 != 0 and num2 % 2 == 0 and num3 % 2 == 0:
				print "\nSe ingresaron 2 números pares."
			else:
				if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 == 0:
					print "\nSe ingresó un número par."
				else:
					if num1 % 2 == 0 and num2 % 2 != 0 and num3 % 2 != 0:
						print "\nSe ingresó un número par."
					else:
						if num1 % 2 != 0 and num2 % 2 == 0 and num3 % 2 != 0:
							print "\nSe ingresó un solo número par."
						else:
							if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0:
								print "\nNO se han ingresado números pares."
resultado = num1 * num2 * num3
print "\nEl resultado de la multiplicación es: ", resultado
if resultado % 3 == 0:
    print "\nEl resultado de la multiplicación: ", resultado, "es multiplo de 3."
else:
   	print "\nEl resultado de la multiplicación: ", resultado, "NO es multiplo de 3"
   	
raw_input("\nOprima la tecla ENTER para finalizar.")