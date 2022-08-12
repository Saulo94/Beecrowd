var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var [inicio, fim] = lines.map(Number);

if (inicio > fim)
    [inicio, fim] = [fim, inicio];

var soma_numeros = 0;

for (let numero = inicio; numero <= fim; numero++) {
    if (numero % 13 !== 0)
        soma_numeros += numero;
}

console.log(soma_numeros);
