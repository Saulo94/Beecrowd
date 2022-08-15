#include <bits/stdc++.h>
using namespace std;

int main(){
  int preco, parcelas, resto, divisao, i;

  cin >> preco;
  cin >> parcelas;

  resto = preco % parcelas;
  divisao = preco / parcelas;

  for(i = 0; i < resto; i++){cout << divisao + 1 << "\n";}
  for(i = 0; i < parcelas - resto; i++){cout << divisao << "\n";}

  return 0;
}
