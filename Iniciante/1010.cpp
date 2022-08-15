#include <bits/stdc++.h>
using namespace std;

int main(){
  double peca1[3], peca2[3], total;

  for(int i = 0; i < 3; i++){
      cin >> peca1[i];
  }
  for(int i = 0; i < 3; i++){
      cin >> peca2[i];
  }

  total = peca1[1] * peca1[2] + peca2[1] * peca2[2];
  cout << fixed << showpoint;
  cout << "VALOR A PAGAR: R$ " << setprecision(2) << total << "\n";

  return 0;
}
