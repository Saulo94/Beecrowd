#include <bits/stdc++.h>
using namespace std;

int main(){
  vector<float> notas(7);
  float dificuldade, maior, menor, soma;
  int quantidade, i, j, i_maior, i_menor;
  string nome;

  cin >> quantidade;

  for(i = 0; i < quantidade; i++){
    cin.ignore();
    getline(cin, nome);
    cin >> dificuldade;

    cin >> notas[0];
    maior = notas[0];
    menor = notas[0];
    i_maior = 0;
    i_menor = 0;

    for(j = 1; j < 7; j++){
      cin >> notas[j];
      if(notas[j] > maior){
        maior = notas[j];
        i_maior = j;
      }
      if(notas[j] < menor){
        menor = notas[j];
        i_menor = j;
      }
    }
    notas[i_maior] = 0;
    notas[i_menor] = 0;

    soma = 0;
    for(j = 0; j < notas.size(); j++){
      soma += notas[j];
    }
    soma *= dificuldade;
    cout << fixed << setprecision(2);
    cout << nome << " " << soma <<"\n";
  }

  return 0;
}
