#include <bits/stdc++.h>
using namespace std;

int main(){
  double a = 0, b = 0, c = 0;
  cin >> a >> b >> c;

  cout << fixed << setprecision(3);
  cout << "TRIANGULO: " << a * c / 2.0 << "\n";
  cout << "CIRCULO: " << 3.14159 * c * c << "\n";
  cout << "TRAPEZIO: " << (a + b) * c / 2.0 << "\n";
  cout << "QUADRADO: " << b * b << "\n";
  cout << "RETANGULO: " << a * b << "\n";

  return 0;
}
