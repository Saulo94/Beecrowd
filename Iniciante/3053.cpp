#include <bits/stdc++.h>
using namespace std;

char Movimento(char _copo, int _mov){
  if(_mov == 1){
    if(_copo == 'A'){return 'B';}
    else if(_copo == 'B'){return 'A';}
  }
  else if(_mov == 2){
    if(_copo == 'B'){return 'C';}
    else if(_copo == 'C'){return 'B';}
  }
  else{
    if(_copo == 'A'){return 'C';}
    else if(_copo == 'C'){return 'A';}
  }

  return _copo;
}

int main(){
  int quant_mov, mov;
  char copo;
  cin >> quant_mov;
  cin >> copo;

  for(int i = 0; i < quant_mov; i++){
    cin >> mov;
    copo = Movimento(copo, mov);
  }

  cout << copo << "\n";

  return 0;
}
