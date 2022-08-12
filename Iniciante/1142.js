var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

numero = parseInt(lines[0]);
k = 1;
for (let i = 0; i < numero; i++) {
    itens = Array();
    for (let j = k; j < k + 3; j++) {
        itens.push(j);
    }
    itens.push("PUM");
    saida = itens.join(" ");
    console.log(saida);
    k += 4;
}