#include <bits/stdc++.h>
using namespace std;

vector<int> v_casas;

int achar_id(int casa){
  auto it = find(v_casas.begin(), v_casas.end(), casa);

  return distance(v_casas.begin(), it);
}

int main(){
  int qt_casas, qt_encomendas, casa, casa_id, ultimo_id, distancia;

  cin >> qt_casas >> qt_encomendas;

  while(qt_casas--){
    cin >> casa;
    v_casas.push_back(casa);
  }

  cin >> casa;
  distancia = ultimo_id = achar_id(casa);
  qt_encomendas--;
  
  while(qt_encomendas--){
    cin >> casa;
    casa_id = achar_id(casa);
    distancia += fabs(casa_id - ultimo_id);
    ultimo_id = casa_id;
  }

  cout << distancia << "\n";

  return 0;
}
