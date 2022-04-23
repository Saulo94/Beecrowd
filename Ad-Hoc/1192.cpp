#include <bits/stdc++.h>
using namespace std;

int main(){
    string entrada;
    //array<char, 3> entrada;
    int qt_casos, resultado, num1, num2;
    int i;

    cin >> qt_casos;

    for(i = 0; i < qt_casos; i++){
        cin >> entrada;
        num1 = entrada[0] - '0';
        num2 = entrada[2] - '0';

        if (num1 == num2){
            resultado = num2 * num1;
        }
        else if (entrada[1] >= 65 && entrada[1] <= 90){
            resultado = num2 - num1;
        }
        else {
            resultado = num2 + num1;
        }
        cout << resultado << "\n";
    }

    return 0;
}