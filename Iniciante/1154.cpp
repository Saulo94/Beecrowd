#include <bits/stdc++.h>
using namespace std;

int main(){
  int idade, soma = 0, i = 0;

  cin >> idade;
  while(idade > 0){
    soma += idade; i++;
    cin >> idade;
  }

  cout << fixed << setprecision(2);
  cout << (double) soma / i << "\n";

  return 0;
}
