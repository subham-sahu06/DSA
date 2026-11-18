#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        int n;
        string s;
        cin >> n >> s;
        int diff[27] = {0};
        for (int i = 0; i < n / 2; i++) {
            int u = s[i] - 'a', v = s[n - 1 - i] - 'a';
            if (u > v) swap(u, v);
            if (u < v) {
                diff[u + 1]++;
                diff[v + 1]--;
            }
        }
        int cur = 0, ans = 0;
        for (int c = 0; c < 26; c++) {
            cur += diff[c];
            if (cur > 0) ans++;
        }
        cout << ans << '\n';
    }
}
