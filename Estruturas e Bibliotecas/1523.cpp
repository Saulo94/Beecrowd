#include <bits/stdc++.h>
using namespace std;

int main(){
  int i, entrada, saida, qt_mot, qt_car, resposta;

  cin >> qt_mot >> qt_car;
  while((qt_mot != 0) && (qt_car != 0)){
    vector<vector<int>> momentos;
    stack<int> estacionamento;

    for(i = 0; i < qt_mot; i++){
      cin >> entrada >> saida;
      momentos.push_back({entrada, 1, i});
      momentos.push_back({saida, 0, i});
    }

    sort(momentos.begin(), momentos.end());
    resposta = 1;
    for(i = 0; i < qt_mot * 2; i++){
      if((momentos[i][1] == 1) && (estacionamento.size() == qt_car)){
        resposta = 0;
        break;
      }
      if((momentos[i][1] == 1) && (estacionamento.size() != qt_car)){
        estacionamento.push(momentos[i][2]);
        continue;
      }
      if(momentos[i][2] == estacionamento.top())
        estacionamento.pop();
      else{
        resposta = 0;
        break;
      }
    }
    if(resposta == 1)
      cout << "Sim\n";
    else
      cout << "Nao\n";

    cin >> qt_mot >> qt_car;
  }
  return 0;
}
