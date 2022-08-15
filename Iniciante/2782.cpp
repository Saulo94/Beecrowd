#include <bits/stdc++.h>
using namespace std;

int main(){
  int quant, numero, i, esc = 0, d;
  vector<int> lista;

  cin >> quant;
  for(i = 0; i < quant; i++){
    cin >> numero;
    lista.push_back(numero);
  }
  if(quant == 1){
    cout << "1\n";
  }
  else{
    d = lista[0] - lista[1];
    esc++;
    for(i = 1; i < quant - 1; i++){
      if(lista[i] - lista[i + 1] != d){
        esc++;
        d = lista[i] - lista[i + 1];
        //cout << d << "\n";
      }
    }
    cout << esc << "\n";
  }

  return 0;
}
