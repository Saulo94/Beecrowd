#include <bits/stdc++.h>
using namespace std;

int main(){
  int codigo, a = 0, g = 0, d = 0;
  cin >> codigo;

  while (codigo != 4){
    while((codigo < 1) || (codigo > 4)){
      cin >> codigo;
    }

    if(codigo == 1){
      a++;
    }
    else if(codigo == 2){
      g++;
    }
    else if(codigo == 3){
      d++;
    }

    cin >> codigo;
  }

  cout << "MUITO OBRIGADO\n";
  cout << "Alcool: " << a << "\n";
  cout << "Gasolina: " << g << "\n";
  cout << "Diesel: " << d << "\n";


  return 0;
}
