#include <bits/stdc++.h>
using namespace std;

int main(){
  char nome[30] = "";
  double salario = 0, vendas = 0;

  cin >> nome;
  cin >> salario;
  cin >> vendas;

  cout << fixed << showpoint;
  cout << "TOTAL = R$ " << setprecision(2) << salario + vendas * 0.15 << "\n";

  return 0;
}
