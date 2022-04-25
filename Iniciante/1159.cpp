#include<bits/stdc++.h>
using namespace std;

int main(){
    int i, soma, numero;

    cin >> numero;
    while(numero){
        if (numero % 2 == 1 || numero % 2 == -1)
            numero += 1;
        
        for(soma = 0, i = numero; i <= numero + 8; i += 2)
            soma += i;
        
        cout << soma << "\n";

        cin >> numero;
    }

    return 0;
}
