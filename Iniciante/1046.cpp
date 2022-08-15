#include <bits/stdc++.h>
using namespace std;

int main(){

  int horaI, horaF;

  cin >> horaI >> horaF;

  if(horaF <= horaI){
    cout << "O JOGO DUROU " << horaF - horaI + 24 << " HORA(S)\n";
  }
  else{
    cout << "O JOGO DUROU " << horaF - horaI << " HORA(S)\n";
  }

  return 0;
}
