#include <bits/stdc++.h>
using namespace std;

int main(){
    int i, k, qt_casos, a, b, temp, soma;

    cin >> qt_casos;
    for(i = 0; i < qt_casos; i++){
        soma = 0;
        cin >> a >> b;
        if (b < a){
            temp = a;
            a = b;
            b = temp;
        }

        for(k = a + 1; k < b; k++){
            if (k % 2 == 1)
                soma += k;
        }

        cout << soma << "\n";
    }

    return 0;
}