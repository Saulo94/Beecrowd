#include<bits/stdc++.h>
using namespace std;

int main(){
    int i, x, y;

    cin >> x >> y;

    for(i = 1; i <= y; i++){
        if (i % x == 0)
            cout << i << "\n";
        else
            cout << i << " ";
    }

    return 0;
}
