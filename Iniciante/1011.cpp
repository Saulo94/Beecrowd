#include <bits/stdc++.h>
using namespace std;

int main(){
  double raio = 0, volume = 0;
  cin >> raio;
  volume = (4.0/3) * 3.14159 * raio * raio * raio;
  cout << fixed << showpoint;
  cout << "VOLUME = " << setprecision(3) << volume << "\n";
}
