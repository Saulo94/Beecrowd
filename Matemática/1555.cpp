#include <bits/stdc++.h>
using namespace std;

int main(){
  int quantidade, x, y, rafa, beto, carlos;

  cin >> quantidade;
  for(int i = 0; i < quantidade; i++){
    cin >> x >> y;

    rafa = 9*x*x + y*y;
    beto = 2*x*x + 25*y*y;
    carlos = -100*x + y*y*y;

    if((rafa > beto) && (rafa > carlos)) printf("Rafael ganhou\n");
    else if((beto > carlos) && (beto > rafa)) printf("Beto ganhou\n");
    else printf("Carlos ganhou\n");
  }
  return 0;
}
