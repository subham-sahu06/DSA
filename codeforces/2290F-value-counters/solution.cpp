#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> p(n, 0);
        bool ok = true;
        for (int v = 1; v <= n; v++) {
            int b;
            cin >> b;
            int i = b + n - v;
            if (!ok) continue;
            if (i < 0 || i >= n || p[i] != 0) ok = false;
            else p[i] = v;
        }
        if (!ok) {
            cout << -1 << '\n';
            continue;
        }
        for (int i = 0; i < n; i++) cout << p[i] << (i + 1 < n ? ' ' : '\n');
    }
}
