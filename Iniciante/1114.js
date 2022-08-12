var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const senha_valida = "2002";

for(var i = 0; i < lines.length; i++){
    senha = lines[i];

    if (senha == senha_valida)
        console.log("Acesso Permitido");
    else
        console.log("Senha Invalida");
}