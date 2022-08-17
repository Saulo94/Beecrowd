var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n').map(Number);

var qt_pessoas = null;
var qt_pedidos = null;

var i = 0;
var qt_casos = lines[i];
while (qt_casos != 0){
    const i_atual = i;
    while (i < i_atual + qt_casos){
        i++;

        qt_pessoas = lines[i];
        
        if (qt_pessoas % 2 == 0)
            qt_pedidos = (qt_pessoas - 2) * 2 + 2;
        else
            qt_pedidos = (qt_pessoas - 1) * 2 + 1;
        
        console.log(qt_pedidos);
    }
    i++;
    qt_casos = lines[i];
}
