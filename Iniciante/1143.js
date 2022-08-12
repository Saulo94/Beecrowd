var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

limite = parseInt(lines[0]);

var [quadrado, cubo] = [null, null];

for (let numero = 1; numero <= limite; numero++){
    quadrado = Math.pow(numero, 2);
    cubo = Math.pow(numero, 3);
    console.log([numero, quadrado, cubo].join(" "));
}
