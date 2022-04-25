#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<int> nums = {1, 7, 6, 5};
    int i;

    while (nums[0] <= 9){
        cout << "I=" << nums[0] << " J=" << nums[1] << "\n"
             << "I=" << nums[0] << " J=" << nums[2] << "\n"
             << "I=" << nums[0] << " J=" << nums[3] << "\n";

        for(i = 0; i < 4; i++){
            nums[i] += 2;
        }
    }
    return 0;
}