//var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var input = "4\n6\n5\n28\n1";
var lines = input.split('\n');

var quant_casos = parseInt(lines[0]);
var numero = null;
var soma_div = null;

for (let i = 1; i <= quant_casos; i++) {
    numero = parseInt(lines[i]);
    soma_div = 0;

    for (let k = 1; k < numero; k++) {
        if (numero % k == 0)
            soma_div += k
    }

    if (soma_div == numero)
        console.log(numero + " eh perfeito");
    else
        console.log(numero + " nao eh perfeito");
}