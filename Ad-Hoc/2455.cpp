#include <bits/stdc++.h>
using namespace std;

int main(){
  int peso1, peso2, comp1, comp2;
  cin >> peso1 >> comp1 >> peso2 >> comp2;

  if(peso1 * comp1 == peso2 * comp2){
    printf("0\n");
  }
  else{
    if(peso1 * comp1 > peso2 * comp2){
      printf("-1\n");
    }
    else{
      printf("1\n");
    }
  }

  return 0;
}
