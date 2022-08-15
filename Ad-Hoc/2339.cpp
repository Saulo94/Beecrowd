#include <bits/stdc++.h>
using namespace std;

int main(){
  int n_c, n_f, n_f_n;
  cin >> n_c >> n_f >> n_f_n;

  if(n_c * n_f_n <= n_f){
    printf("S\n");
  }
  else{
    printf("N\n");
  }
  return 0;
}
