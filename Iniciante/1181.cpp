#include <bits/stdc++.h>
using namespace std;

int main(){
  float numero, soma = 0;
  int linha, i, j;
  char ope;

  cin >> linha;
  cin >> ope;
  for(i = 0; i < 12; i++){
    if(i != linha){
      for(j = 0; j < 12; j++){
        cin >> numero;
      }
    }
    else{
      for(j = 0; j < 12; j++){
        cin >> numero;
        soma += numero;
      }
      if(ope == 'M'){
        soma /= 12;
      }
      break;
    }
  }
  cout << fixed << setprecision(1);
  cout << soma << "\n";

  return 0;
}
