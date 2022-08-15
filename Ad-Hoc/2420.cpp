#include <bits/stdc++.h>
using namespace std;

int main(){
  int quant, numero, i, total = 0, soma = 0;
  vector<int> lista;

  cin >> quant;
  for(i = 0; i < quant; i++){
    cin >> numero;
    total += numero;
    lista.push_back(numero);
  }
  total /= 2;

  for(i = 0; i < quant, soma < total; i++){
    soma += lista[i];
  }
  printf("%d\n", i);

  return 0;
}
