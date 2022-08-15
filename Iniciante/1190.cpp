#include <bits/stdc++.h>
using namespace std;

int main(){
  float soma = 0, numero;
  int i, j, k;
  char opc;

  cin >> opc;

  for(i = 0, k = 0; i < 6; i++, k++){
    for(j = 0; j < 12 - k; j++){
      cin >> numero;
    }
    for(j = 0; j < k; j++){
      cin >> numero;
      soma += numero;
    }
  }
  for(i = 6, k = 5; i < 12; i++, k--){
    for(j = 0; j < 12 - k; j++){
      cin >> numero;
    }
    for(j = 0; j < k; j++){
      cin >> numero;
      soma += numero;
    }
  }

  if(opc == 'M'){
    soma /= 30;
  }

  cout << fixed << setprecision(1);
  cout << soma <<"\n";

  return 0;
}
