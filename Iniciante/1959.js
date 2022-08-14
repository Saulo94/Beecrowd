var input = require('fs').readFileSync('/dev/stdin', 'utf8');
//var input = "1 3\n";
var lines = input.split('\n');

[numero_lados, comprimento_lados] = lines[0].split(" ").map(Number);

console.log(numero_lados * comprimento_lados);
