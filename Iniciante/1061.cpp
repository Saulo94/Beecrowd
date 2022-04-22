#include <bits/stdc++.h>
using namespace std;

int main(){
    int tempo_inicio, tempo_fim, tempo_decorrido;
    int dia, hora, min, seg;
    string _;

    cin >> _ >> dia;
    tempo_inicio = dia * 24 * 3600;
    cin >> hora >> _ >> min >> _ >> seg;
    tempo_inicio += hora * 3600 + min * 60 + seg;

    cin >> _ >> dia;
    tempo_fim = dia * 24 * 3600;
    cin >> hora >> _ >> min >> _ >> seg;
    tempo_fim += hora * 3600 + min * 60 + seg;

    tempo_decorrido = tempo_fim - tempo_inicio;

    dia = tempo_decorrido / (24 * 3600);
    cout << dia << " dia(s)\n";
    tempo_decorrido -= dia * 24 * 3600;
    hora = tempo_decorrido / 3600;
    cout << hora << " hora(s)\n";
    tempo_decorrido -= hora * 3600;
    min = tempo_decorrido / 60;
    cout << min << " minuto(s)\n";
    tempo_decorrido -= min * 60;
    cout << tempo_decorrido << " segundo(s)\n";

    return 0;
}