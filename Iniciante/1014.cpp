#include <bits/stdc++.h>
using namespace std;

int main(){
  double distancia = 0, litros = 0;

  cin >> distancia;
  cin >> litros;
  cout << fixed << showpoint;
  cout << setprecision(3) << (distancia / litros) << " km/l\n";

  return 0;
}
