#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    int count = 0;
    cin >> S;
    for (int i = 0; i < 3; i++) {
        if (S[i] == '1') {
            count++;
        }
    }
    cout << count << endl;
}
