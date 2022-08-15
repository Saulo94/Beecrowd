#include <bits/stdc++.h>
using namespace std;

int main(){
  int codigo, quant;
  double preco;
  cin >> codigo >> quant;

  if(codigo == 1){
    preco = 4;
  }
  else if(codigo == 2){
    preco = 4.5;
  }
  else if(codigo == 3){
    preco = 5;
  }
  else if(codigo == 4){
    preco = 2;
  }
  else{
    preco = 1.5;
  }
  cout << fixed << setprecision(2);
  cout << "Total: R$ " << preco * quant << "\n";

  return 0;
}
