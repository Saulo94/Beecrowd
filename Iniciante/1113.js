//var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var input = "-86 -92\n36 -61\n57 -27\n2 2";
var lines = input.split('\n');

for(var i = 0; i < lines.length; i++){
    var [num1, num2] = lines[i].split(' ').map(Number);

    if (num1 > num2) {
        console.log("Decrescente");
    }
    else if (num2 > num1) {
        console.log("Crescente");
    }
}
