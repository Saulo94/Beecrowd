#include <bits/stdc++.h>
using namespace std;

int main(){
  vector<int> lista;
  int quant, numero, i;

  cin >> quant;
  for(i = 0; i < quant; i++){
    cin >> numero;
    lista.push_back(numero);
  }
  if(quant == 1){
    printf("%d\n", lista[0]);
  }
  else{
    printf("%d\n", lista[0] + lista[1]);
    for(i = 1; i < quant - 1; i++){
      printf("%d\n", lista[i-1] + lista[i] + lista[i+1]);
    }
    printf("%d\n", lista[quant-1] + lista[quant-2]);
  }
  return 0;
}
