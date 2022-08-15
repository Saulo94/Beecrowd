#include <bits/stdc++.h>
using namespace std;

int main(){
  int tempo = 0, velocidade_media = 0;

  cin >> tempo;
  cin >> velocidade_media;

  cout << fixed << showpoint;
  cout << setprecision(3) << tempo * velocidade_media / 12.0 << "\n";

  return 0;
}
