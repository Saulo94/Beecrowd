#include <bits/stdc++.h>
using namespace std;

int main(){
  double salario, reajuste;
  cin >> salario;

  if(salario <= 400){
    reajuste = 0.15;
  }
  else if((salario > 400) && (salario <= 800)){
    reajuste = 0.12;
  }
  else if((salario > 800) && (salario <= 1200)){
    reajuste = 0.1;
  }
  else if((salario > 1200) && (salario <= 2000)){
    reajuste = 0.07;
  }
  else{
    reajuste = 0.04;
  }

  cout << fixed << setprecision(2);
  cout << "Novo salario: " << salario * reajuste + salario << "\n";
  cout << "Reajuste ganho: " << salario * reajuste << "\n";
  cout << "Em percentual: " << setprecision(0) << reajuste * 100 << " %\n";

  return 0;
}
