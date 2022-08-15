#include <bits/stdc++.h>
using namespace std;

int main(){
  int quantidade, i, contador, contador2;
  
  char objeto;
  cin >> quantidade;
  getchar();
  while(quantidade--){
    contador = contador2 = 0;
    objeto = getchar();
    while(objeto != '\n'){
      if(objeto == '<') contador++;
      else if((objeto == '>') && (contador > 0)){
        contador--;
        contador2++;
      }
      objeto = getchar();
    }
    cout << contador2 << "\n";
  }

  return 0;
}
