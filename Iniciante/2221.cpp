#include <bits/stdc++.h>
using namespace std;

int main(){
  int quantidade, ataqueD, ataqueG, defesaD, defesaG, levelD, levelG, bonus;
  float golpeD, golpeG;

  cin >> quantidade;
  for(int i = 0; i < quantidade; i++){
    cin >> bonus;
    cin >> ataqueD >> defesaD >> levelD;
    cin >> ataqueG >> defesaG >> levelG;

    if(levelD % 2 == 0) golpeD = ((ataqueD + defesaD) / 2.0) + bonus;
    else golpeD = ((ataqueD + defesaD) / 2.0);
    if(levelG % 2 == 0) golpeG = ((ataqueG + defesaG) / 2.0) + bonus;
    else golpeG = ((ataqueG + defesaG) / 2.0);

    if(golpeD > golpeG) cout << "Dabriel\n";
    else if(golpeD < golpeG) cout << "Guarte\n";
    else cout << "Empate\n";
  }

  return 0;
}
