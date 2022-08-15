#include <bits/stdc++.h>
using namespace std;

int main(){
  long int segundos = 0;
  int horas = 0, minutos = 0;
  cin >> segundos;
  minutos = segundos / 60;
  segundos = segundos % 60;
  horas = minutos / 60;
  minutos = minutos % 60;

  cout << horas << ":" << minutos << ":" << segundos << "\n";

  return 0;
}
