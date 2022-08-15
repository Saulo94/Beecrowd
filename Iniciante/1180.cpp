#include <bits/stdc++.h>
using namespace std;

int main(){
  int menor, im, quant, numero;
  cin >> quant;
  cin >> menor;
  im = 0;
  for(int i = 1; i < quant; i++){
    cin >> numero;
    if(numero < menor){
      menor = numero;
      im = i;
    }
  }

  cout << "Menor valor: " << menor << "\n";
  cout << "Posicao: " << im << "\n";

  return 0;
}
