#coding=UTF-8

""" UdemyBucles: Ejercicio N°18 - Hacer un programa que muestre un 
cronometro, indicando las horas, minutos y segundos."""

import os
import time

for hora in range(0, 24):
	for minutos in range(0, 60):
		for segundo in range(0, 60):
			print hora, minutos, segundo
			time.sleep(1)
raw_input("Oprima ENTER para finalizar el programa.")