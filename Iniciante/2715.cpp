#include <bits/stdc++.h>
using namespace std;

int main(){
  vector<int> trabalhos;
  long long int quantidade, numero, i, j, soma_i, soma_j, soma;

  while(cin >> quantidade){
    trabalhos.clear();
    soma_i = soma_j = soma = 0;

    while(quantidade--){
      cin >> numero;
      soma += numero;
      trabalhos.push_back(numero);
    }

    for(i = 0, j = trabalhos.size() - 1; i < trabalhos.size(), j >= 0;){
      if(soma_i + soma_j == soma) break;
      if(soma_i <= soma_j){
        soma_i += trabalhos[i];
        i++;
      }
      else{
        soma_j += trabalhos[j];
        j--;
      }
    }
    cout << fabs(soma_i - soma_j) << "\n";
  }

  return 0;
}
