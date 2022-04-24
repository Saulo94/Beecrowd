#include <bits/stdc++.h>
using namespace std;

int main(){
    string palavra1, palavra2;
    vector<char> palavra3;
    int i, k, max_tamanho, qt_casos;

    cin >> qt_casos;

    for(k = 0; k < qt_casos; k++){
        cin >> palavra1 >> palavra2;

        //Guardando o tamanho da maior string
        if (palavra1.length() > palavra2.length())
            max_tamanho = palavra1.length();
        else
            max_tamanho = palavra2.length();

        //Gerrando a string final
        for(i = 0; i < max_tamanho; i++){
            if (i < palavra1.length())
                palavra3.push_back(palavra1[i]);
            if (i < palavra2.length())
                palavra3.push_back(palavra2[i]);
        }

        //Printando a string final
        for(i = 0; i < palavra3.size(); i++)
            cout << palavra3[i];
        cout << "\n";
        palavra3.clear();
    }   
    return 0;
}
