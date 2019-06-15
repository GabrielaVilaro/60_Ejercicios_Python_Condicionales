#coding=UTF-8

#Ejemplo de objetos del tutorial sobre Python de "Pildoras informáticas."

class coche():

	def __init__(self): #este es el constructor da un estado inicial a los objetos pertenecientes a la clase
																						#coche en este caso
		self.largoChasis = 250  #propiedades del coche (caracteristicas)
		self.anchoChasis = 120
		self.ruedas = 4 #se encapsula con dos guiones bajos. no se puede cambiar por fuera.
		self.enMarcha = False 

	def arrancar (self): 
							 #self es como this es javascript. se refiere al objeto , contexto
		self.enMarcha = True   #self seria " este coche" hace referencia al propio objeto
	
	def estado(self):
		if self.enMarcha:
			return "El coche esta en marcha" 
		else:
			return "El coche está apagado"
						  					  

miCoche = coche()


print "El largo del chasis del coche es: ", miCoche.largoChasis #para acceder a alguna propiedad del objeto.

print "El coche tiene: ", miCoche.ruedas, "ruedas."

miCoche.arrancar() #llamamos a la función arrancar

print miCoche.estado() #arrancado o apagado

print "A continuación creamos el segundo objeto"

miCoche2 = coche() #pertenece a la misma clase, o sea "coche".

print "El largo del chasis del coche 2 es: ", miCoche2.largoChasis  #para acceder a alguna propiedad del objeto.

print "El coche 2 tiene: ", miCoche2.ruedas

print miCoche2.estado() #estado sería apagado o arrancado, este estaría apagado.

raw_input("Oprima ENTER para finalizar el programa.")
