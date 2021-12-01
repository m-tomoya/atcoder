#include <bits/stdc++.h>
using namespace std;

int main() {
    string r;
    string g;
    string b;
    string s;
    cin >> r >> g >> b;
    s = r + g + b;
    cout << s << endl;
    int t = atoi(s.c_str());
    if (t % 4 == 0) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}
