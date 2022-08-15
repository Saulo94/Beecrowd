#include <bits/stdc++.h>
using namespace std;

int tam, somas, i, j;

int calcular_linha(vector<vector<int>> q){
  vector<int> somas(tam);
  for(i = 0; i < tam; i++){
    somas[i] = 0;
    for(j = 0; j < tam; j++){
      somas[i] += q[i][j];
    }
  }
  for(i = 0; i < tam - 1; i++){
    if(somas[i] != somas[i + 1]){
      return -1;
    }
  }
  return somas[0];
}

int calcular_coluna(vector<vector<int>> q){
  vector<int> somas(tam);
  for(i = 0; i < tam; i++){
    somas[i] = 0;
    for(j = 0; j < tam; j++){
      somas[i] += q[j][i];
    }
  }
  for(i = 0; i < tam - 1; i++){
    if(somas[i] != somas[i + 1]){
      return -1;
    }
  }
  return somas[0];
}

int calcular_diagonal1(vector<vector<int>> q){
  somas = 0;
  for(i = 0;i < tam; i++){
    somas += q[i][i];
  }
  return somas;
}

int calcular_diagonal2(vector<vector<int>> q){
  somas = 0;
  for(i = 0; i < tam; i++){
    somas += q[i][tam - i - 1];
  }
  return somas;
}

int main(){
  int numero, soma_l, soma_c, soma_d1, soma_d2;
  cin >> tam;
  vector<vector<int>> quadrado(tam, vector<int>(tam));

  for(i = 0; i < tam; i++){
    for(j = 0; j < tam; j++){
      cin >> numero;
      quadrado[i][j] = numero;
    }
  }

  soma_l = calcular_linha(quadrado);
  soma_c = calcular_coluna(quadrado);
  soma_d1 = calcular_diagonal1(quadrado);
  soma_d2 = calcular_diagonal2(quadrado);

  if((soma_c == soma_l) && (soma_c == soma_d1) && (soma_c == soma_d2)){
    cout << soma_c << "\n";
  }
  else{
    cout << "-1\n";
  }

  return 0;
}
