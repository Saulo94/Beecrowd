#include <bits/stdc++.h>
using namespace std;

int main(){
  int ordem, i, j;

  while(cin >> ordem){
    for(i = 0; i < ordem; i++){
      for(j = 0; j <ordem; j++){
        if((i == j) && (ordem - 1 - j != i)){
          cout << 1;
        }
        else if(ordem - 1 - j == i){
          cout << 2;
        }
        else{
          cout << 3;
        }
      }
      cout << "\n";
    }
  }
  return 0;
}
