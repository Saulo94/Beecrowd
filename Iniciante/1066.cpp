#include <bits/stdc++.h>
using namespace std;

int main(){
    int qt_par = 0, qt_impar = 0, qt_pos = 0, qt_neg = 0;
    int i, numero;

    for(i = 0; i < 5; i++){
        cin >> numero;
        if (numero % 2 == 0)
            qt_par++;
        else
            qt_impar++;
        if (numero > 0)
            qt_pos++;
        else if(numero < 0)
            qt_neg++;
    }

    cout << qt_par << " valor(es) par(es)\n";
    cout << qt_impar << " valor(es) impar(es)\n";
    cout << qt_pos << " valor(es) positivo(s)\n";
    cout << qt_neg << " valor(es) negativo(s)\n";

    return 0;
}