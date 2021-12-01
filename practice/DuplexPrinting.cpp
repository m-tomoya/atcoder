#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    int total;
    cin >> N;
    if (N % 2 == 0) {
        total = N / 2;
    } else {
        total = N / 2 + 1;
    }
    cout << total << endl;
}
