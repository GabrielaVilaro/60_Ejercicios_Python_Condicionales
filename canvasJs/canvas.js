var d = document.getElementById("dibujo"); //elijo el elemento

var lienzo = d.getContext("2d"); //dibujo en 2d

var lineas = 30;

var l = 0;

var yi, xf;

while(l < lineas) { //30 líneas en el mismo luagar

	yi = 10 * l;

	xf = 10 * (l + 1);

	dibujar_lineas("grey", 0, yi, xf, 500);

	l = l + 2;
}


lienzo.beginPath(); //empezar un trazo

lienzo.strokeStyle = "red";

lienzo.moveTo(100, 10); //mueve el "lapiz"

lienzo.lineTo(290, 200); //trazar línea

lienzo.stroke();

lienzo.closePath(); //finalizar camino

lienzo.beginPath(); //empezar un trazo

lienzo.strokeStyle = "blue";

lienzo.moveTo(100, 100); //mueve el "lapiz"

lienzo.lineTo(200, 200); //trazar línea

lienzo.stroke();

lienzo.closePath(); //finalizar camino


//voy a crear una función que facilite esto

function dibujar_lineas(color, xinicial, yinicial, xfinal, yfinal) {
	lienzo.beginPath(); //empezar un trazo

lienzo.strokeStyle = color;

lienzo.moveTo(xinicial, yinicial); //mueve el "lapiz"

lienzo.lineTo(xfinal, yfinal); //trazar línea

lienzo.stroke();

lienzo.closePath(); //finalizar camino

}

dibujar_lineas("green", 80, 100, 300, 300);
