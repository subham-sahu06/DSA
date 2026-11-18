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
        vector<vector<int>> g(n + 1);
        for (int i = 0; i < n - 1; i++) {
            int u, v;
            cin >> u >> v;
            g[u].push_back(v);
            g[v].push_back(u);
        }
        vector<int> par(n + 1, 0), order, sz(n + 1, 0);
        order.reserve(n);
        order.push_back(1);
        for (int i = 0; i < (int)order.size(); i++) {
            int x = order[i];
            for (int y : g[x]) {
                if (y != par[x]) {
                    par[y] = x;
                    order.push_back(y);
                }
            }
        }
        for (int i = n - 1; i >= 0; i--) {
            int x = order[i];
            sz[x]++;
            if (par[x]) sz[par[x]] += sz[x];
        }
        int lo = 0, hi = n;
        vector<int> heavy(n + 1);
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            fill(heavy.begin(), heavy.end(), 0);
            bool ok = true;
            for (int i = 1; i < n && ok; i++) {
                int x = order[i];
                if (sz[x] > mid) {
                    int p = par[x];
                    heavy[p]++;
                    if (heavy[p] > (p == 1 ? 2 : 1)) ok = false;
                }
            }
            if (ok) hi = mid;
            else lo = mid + 1;
        }
        cout << n - lo << '\n';
    }
}
