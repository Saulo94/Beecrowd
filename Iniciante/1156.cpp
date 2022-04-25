#include<bits/stdc++.h>
using namespace std;

int main(){
    double den, num, soma = 0;

    for(num = 1, den = 0; num <= 39; num += 2, den++)
        soma += num / pow(2, den);

    cout << setprecision(2) << fixed;
    cout << soma << "\n";

    return 0;
}
