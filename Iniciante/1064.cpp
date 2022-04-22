#include <bits/stdc++.h>
using namespace std;

int main(){
    int qt_pos = 0;
    double soma = 0, numero;
    int i;

    for(i = 0; i < 6; i++){
        cin >> numero;
        if (numero > 0){
            soma += (double) numero;
            qt_pos++;
        }
    }

    cout << fixed << setprecision(1);
    cout << qt_pos << " valores positivos\n";
    cout << soma / (double) qt_pos << "\n";
    return 0;
}