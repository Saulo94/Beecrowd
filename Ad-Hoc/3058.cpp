#include <bits/stdc++.h>
using namespace std;

int main(){
  int quant, gramas;
  double preco, menor_preco = 1e7;

  cin >> quant;
  
  for(int i = 0; i < quant; i++){
    cin >> preco;
    cin >> gramas;

    preco = 1000 * preco / gramas;
    if(preco < menor_preco){
      menor_preco = preco;
    }
  }

  cout << fixed << setprecision(2);
  cout << menor_preco << "\n";

  return 0;
}
