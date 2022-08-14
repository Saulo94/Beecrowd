var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

// quantidade de estrelas
var qt_estrelas = parseInt(lines[0]);

// lista de quantidade de carneiros por estrela
var estrelas = lines[1].split(" ").map(Number);

// para guardar os índices das estrelas visitadas
var estrelas_visitadas = new Set();

// quantidade de carneiros da estrela atual
var qt_carneiros_estrela = null;

// indíce da estrela atual
var i_estrela = 0;

// continua até dar break ou o índice da estrela sair do array
while (i_estrela >= 0 && i_estrela < qt_estrelas){
    // registra a estrela como visitada
    estrelas_visitadas.add(i_estrela);

    qt_carneiros_estrela = estrelas[i_estrela];

    // se a estrela não possui carneiro, a jornada para
    if (qt_carneiros_estrela == 0)
        break;

    // decrementa a quantidade de carneiros, pois um foi roubado
    estrelas[i_estrela] = qt_carneiros_estrela - 1;

    // decide para qual estrela adjacente ele irá
    if (qt_carneiros_estrela % 2 == 0)
        i_estrela--;
    else
        i_estrela++;
}

// soma dos carneiros restantes em cada estrela
var qt_carneiros_sobrado = 0;
estrelas.forEach(qt_carneiros => {
    qt_carneiros_sobrado += qt_carneiros;
});

// exibe quantidade de estrelas visitadas e quantidade de carneiros sobrados
console.log(estrelas_visitadas.size, qt_carneiros_sobrado);
