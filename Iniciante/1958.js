var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var numero = lines[0];

var sinal_numero = null;
if (numero[0] == "-")
    sinal_numero = "-";
else
    sinal_numero = "+";

numero = Math.abs(parseFloat(numero));

var qt_operacoes = 0;
var expoente = "E";
if (numero != 0){
    if (numero < 1){
        expoente += "-";
        while (numero < 1){
            numero *= 10;
            qt_operacoes++;
        }
    } else if (numero >= 10){
        expoente += "+";
        while(numero > 10){
            numero /= 10;
            qt_operacoes++;
        }
    } else
        expoente += "+";
} else
    expoente += "+";

if (qt_operacoes < 10)
    expoente += "0" + qt_operacoes;
else
    expoente += qt_operacoes;

var palavra = sinal_numero + numero.toFixed(4) + expoente;

console.log(palavra);
