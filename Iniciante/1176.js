var hashMap = {};

function fibonaci(numero){
    if (hashMap[numero])
        return hashMap[numero];
    
    if (numero == 0)
        return 0;
    else if (numero == 1 || numero == 2)
        return 1;
    else{
        resultado = fibonaci(numero - 2) + fibonaci(numero - 1);
        hashMap[numero] = resultado;
        return resultado;
    }

}

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
//var input = "6\n10\n1\n2\n3\n4\n5";
var lines = input.split('\n');

var quant_casos = parseInt(lines[0]);
var numero = null;

for (let i = 1; i <= quant_casos; i++) {
    numero = parseInt(lines[i]);

    console.log("Fib(" + numero + ") = " + fibonaci(numero));
}