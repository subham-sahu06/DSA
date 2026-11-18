#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        vector<int> pre(n + 1, 0);
        int total = 0;
        for (int i = 1; i <= n; i++) {
            long long a;
            cin >> a;
            int lo = max(1, i - k);
            int x = pre[i - 1] ^ pre[lo - 1];
            int g = x == 0 ? 1 : 0;
            pre[i] = pre[i - 1] ^ g;
            if (a & 1) total ^= g;
        }
        cout << (total ? "Alice" : "Bob") << '\n';
    }
}
