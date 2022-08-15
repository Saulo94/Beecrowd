#include <bits/stdc++.h>
using namespace std;

int main(){
  int quantidade, numero, i;
  cin >> quantidade;
  while (quantidade != 0) {
    queue<int> cartas;
    vector<int> descartadas;

    for(i = 1;i <= quantidade; i++) cartas.push(i);
    while(cartas.size() > 1){
      descartadas.push_back(cartas.front());
      cartas.pop();
      numero = cartas.front();
      cartas.pop();
      cartas.push(numero);
    }

    cout << "Discarded cards: ";
    if(quantidade > 1){
      for(i = 0; i < quantidade - 2; i++) cout << descartadas[i] << ", ";
      cout << descartadas[quantidade - 2];
    }
    cout << "\n";

    cout << "Remaining card: " << cartas.front() << "\n";
    cin >> quantidade;
  }

  return 0;
}
