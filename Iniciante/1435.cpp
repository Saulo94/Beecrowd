#include <bits/stdc++.h>
using namespace std;

int main(){
  int ordem = -1, i, j, minimo;
  vector<int> valores(4);
  while(ordem != 0){
    cin >> ordem;

    for(i = 0; i < ordem; i++){
      for(j = 0; j < ordem - 1; j++){
        valores[0] = j;
        valores[1] = ordem - 1 - j;
        valores[2] = i;
        valores[3] = ordem - 1 - i;
        minimo = *min_element(valores.begin(), valores.end());
        printf("%3d ", minimo + 1);
      }
      printf("  1\n");
    }
    if(ordem != 0){
      printf("\n");
    }
  }
  return 0;
}
