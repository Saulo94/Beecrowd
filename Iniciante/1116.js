var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

quant_lines = parseInt(lines[0]);

var [num1, num2] = [null, null];

for(var i = 1; i <= quant_lines; i++){
    [num1, num2] = lines[i].split(' ').map(Number);

    if (num2 === 0)
        console.log("divisao impossivel");
    else
        console.log((num1 / num2).toFixed(1));
}