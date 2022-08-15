#include <bits/stdc++.h>
using namespace std;

int main(){
  int numero = 0, horas = 0;
  float salario_hora = 0, salario_total = 0;

  cin >> numero;
  cin >> horas;
  cin >> salario_hora;

  salario_total = salario_hora * horas;

  cout << fixed << showpoint;
  cout << "NUMBER = " << numero << "\n";
  cout << "SALARY = U$ " << setprecision(2) << salario_total << "\n";
  return 0;
}
