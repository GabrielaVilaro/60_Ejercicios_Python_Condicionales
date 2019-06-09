#coding=UTF-8


'''
Ejercicio: 23, Tema: Toma de desiciones
Enunciado --> (23.) Ingresar las ventas totales que efectuó un empleado durante una quincena. Informar la comisión que
le corresponde en pesos según sea el caso: si 0 < ventas <= $ 5000 no tiene comisión; si $ 5000 <
ventas <= $ 10000 comisión del 8% sobre las ventas; si ventas > $ 10000 comisión del 5% sobre la
diferencia entre la venta total y $ 10000, más $ 800 fijos.
Nombre del archivo 'td23.py'
Desarrollo del algoritmo en código Python
'''
print "Informa la comisión correspondiente según las ventas efectuadas por el empleado."

ventas = raw_input("\nIngrese las ventas totales que efectuó el empleado en esta quincena: ")
ventas = int(ventas)

def comision_ventas(parte, todo):
    return parte * todo / 100

def diferencia(num1, num2): 
    return num1 % num2


if ventas > 0 and ventas <= 5000:
    print "\nEl empleado no tiene comisión."
else:
    if ventas > 5000 and ventas <= 10000:
        print "\nLa comisión es de un %8, corresponde: " "$", comision_ventas (8, ventas)
    else:
        if ventas > 10000:
            print "\nLa comisión es de $800 fijos + : " "$" , comision_ventas (5, diferencia(10000, ventas))

raw_input("\nPresione la tecla ENTER para finalizar.")