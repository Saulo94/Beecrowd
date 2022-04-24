#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<float> j = {1, 2, 3};
    double i;
    int k;

    for(i = 0; i <= 2; i += 0.2){
        cout << "I=" << i << " J=" << j[0] << "\n"
             << "I=" << i << " J=" << j[1] << "\n"
             << "I=" << i << " J=" << j[2] << "\n";
        for(k = 0; k < 3; k++){
            j[k] += 0.2;
        }
    }

    return 0;
}
