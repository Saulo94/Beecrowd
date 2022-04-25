#include<bits/stdc++.h>
using namespace std;

int main(){
    double i, soma = 0;

    for(i = 1; i <= 100; i++)
        soma += 1 / i;

    cout << setprecision(2) << fixed;
    cout << soma << "\n";

    return 0;
}
