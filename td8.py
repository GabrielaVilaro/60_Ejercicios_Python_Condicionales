#coding=UTF-8


'''
Ejercicio: 8, Tema: Toma de desiciones
Enunciado --> (8.) Se leen 2 números A y B, y se pide imprimir: -1 si A< 0 y B< 0; 1 si A>0 y B>0; y 0 si A* B<=0.
Nombre del archivo 'td8.py'
Desarrollo del algoritmo en código Python
'''

a = raw_input("\nIngrese el primer número: ")
a = int(a)
b = raw_input("\nIngrese el segundo número: ")
b = int(b)
if a and b < 0: #Imprime - 1 si a y b son menores a 0
	print -1
elif a and b > 0: # imprime 1 si a y b son mayores a 0
	print 1
elif a * b <= 0: #imprime 0 si a por b es menor o igual a 0
	print 0
raw_input("\nOprima la tecla ENTER para finalizar. ")
