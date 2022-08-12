var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var numero = null;
var soma_notas = 0;
var qt_notas_validas = 0;

for (let i = 0; i < lines.length; i++) {
    numero = parseFloat(lines[i]);
    if (numero >= 0 && numero <= 10){
        soma_notas += numero;
        qt_notas_validas++;
    } else
        console.log("nota invalida");
    if (qt_notas_validas == 2)
        break
}
media = soma_notas / 2;
console.log("media = " + media.toFixed(2));
