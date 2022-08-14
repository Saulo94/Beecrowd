// hasmap de sequência por número
var sequenciaByNumero = {};

function get_sequencia(numero){
    /**
     * função recursiva que obtém a sequência dado o número
     */

    // verifica se já não foi obtido a sequência
    if (sequenciaByNumero[numero])
        return sequenciaByNumero[numero];
    
    // valor padrão para zero
    if (numero == 0)
        return [0];

    // gera um array contendo o número 'n' tantas 'n' vezes
    var sequencia = Array();
    for (let i = 0; i < numero; i++)
        sequencia.push(numero);
    
    resultado = get_sequencia(numero - 1).concat(sequencia);

    // guarda a sequencia obtida no hasmap
    sequenciaByNumero[numero] = resultado;

    return resultado;
}

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n').map(Number);


var resultado_sequencia = null;
var quant_numeros = null;
var plural = null;
var numero = null;
var i_caso = 1;
for (let i = 0; i < lines.length - 1; i++) {
    numero = lines[i];
    // valor padrão da variável
    plural = "";

    // sequencia obtida
    resultado_sequencia = get_sequencia(numero);

    // quantidade de números da sequência
    quant_numeros = resultado_sequencia.length;

    // se o tamanho da sequência for maior que 1, acrescenta-se o 's' de plural
    if (quant_numeros != 1)
        plural = "s";

    // printando o resultado
    console.log("Caso %d: %d numero%s", i_caso, quant_numeros, plural);
    console.log(resultado_sequencia.join(" "));
    console.log("");

    // incrementando o número do caso
    i_caso++;
}
