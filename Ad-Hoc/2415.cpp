#include <bits/stdc++.h>
using namespace std;

int main(){
  int quant, numero, un = 0, maximo = 0, pontos;
  cin >> quant;

  for(int i = 0; i < quant; i++){
    cin >> numero;
    if(numero == un){
      pontos++;
    }
    else{
      if(pontos > maximo){
        maximo = pontos;
      }
      pontos = 1;
      un = numero;
    }
  }

  if(pontos > maximo){
    maximo = pontos;
  }

  cout << maximo << "\n";
  return 0;
}
