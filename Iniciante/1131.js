var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var [part_inter, part_gremio, empates] = [0, 0, 0];
var [gols_inter, gols_gremio] = [null, null];
var qt_grenais = 0;

var i = -1;
var escolha = null;
do {
    i++;
    qt_grenais++;

    [gols_inter, gols_gremio] = lines[i].split(' ').map(Number);

    if (gols_inter > gols_gremio)
        part_inter++;
    else if (gols_inter < gols_gremio)
        part_gremio++;
    else
        empates ++;

    console.log("Novo grenal (1-sim 2-nao)");
    i++;
    escolha = lines[i];
} while (escolha == '1')

console.log(qt_grenais + " grenais");
console.log("Inter:" + part_inter);
console.log("Gremio:" + part_gremio);
console.log("Empates:" + empates);

if (part_gremio > part_inter)
    console.log("Gremio venceu mais");
else if (part_gremio < part_inter)
    console.log("Inter venceu mais");
else
    console.log("Nao houve vencedor");