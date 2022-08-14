var input = require('fs').readFileSync('/dev/stdin', 'utf8');
//var input = "14 40 12 60\n";
var lines = input.split('\n');

// largura de cada lado
[a, b, c, d] = lines[0].split(" ").map(Number);

// possibilidades de triângulos
var possibilidades = [[a, b, c], 
                      [a, b, d],
                      [a, c, d],
                      [b, c, d]];

// guarda se possibilidade é triângulo
var eh_triangulo = "N";

// verifica se alguma possibilidade é triângulo
for (let i = 0; i < possibilidades.length; i++) {
    poss = possibilidades[i];

    if ((poss[0] + poss[1] > poss[2]) && (poss[1] + poss[2] > poss[0]) && (poss[0] + poss[2] > poss[1])){
        eh_triangulo = "S";
        break;
    }
}

console.log(eh_triangulo);
