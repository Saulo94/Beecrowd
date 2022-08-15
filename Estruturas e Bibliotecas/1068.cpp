#include <bits/stdc++.h>
using namespace std;

int main(){
  int contador, resposta, i;
  string expressao;
  while(cin >> expressao){
    contador = 0;
    resposta = 1;
    for(i = 0; i < expressao.size(); i++){
      if(expressao[i] == '(')
        contador++;
      else if((expressao[i] == ')') && (contador > 0))
        contador--;
      else if((expressao[i] == ')') && (contador <= 0)){
        resposta = 0;
        break;
      }
    }
    if((contador != 0) || (!resposta)){
      cout << "incorrect\n";
    }
    else{
      cout << "correct\n";
    }
  }
  return 0;
}
