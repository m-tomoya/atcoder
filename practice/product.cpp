#include <bits/stdc++.h>
using namespace std;

int main() {
    int a;
    int b;
    int total;
    cin >> a >> b;
    total = a * b;
    if (total % 2 == 0) {
        cout << "Even" << endl;
    } else {
        cout << "Odd" << endl;
    }
}
