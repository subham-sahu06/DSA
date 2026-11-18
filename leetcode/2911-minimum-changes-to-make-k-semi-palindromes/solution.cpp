class Solution {
public:
    int minimumChanges(string s, int k) {
        int n = s.size();
        const int INF = 1000000;
        vector<vector<int>> cost(n, vector<int>(n, INF));
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int len = j - i + 1;
                for (int d = 1; d < len; d++) {
                    if (len % d != 0) continue;
                    int changes = 0;
                    for (int r = 0; r < d; r++) {
                        int lo = i + r, hi = i + len - d + r;
                        while (lo < hi) {
                            if (s[lo] != s[hi]) changes++;
                            lo += d;
                            hi -= d;
                        }
                    }
                    cost[i][j] = min(cost[i][j], changes);
                }
            }
        }
        vector<vector<int>> dp(k + 1, vector<int>(n + 1, INF));
        dp[0][0] = 0;
        for (int p = 1; p <= k; p++) {
            for (int j = 1; j <= n; j++) {
                for (int i = 0; i < j; i++) {
                    if (dp[p - 1][i] >= INF || cost[i][j - 1] >= INF) continue;
                    dp[p][j] = min(dp[p][j], dp[p - 1][i] + cost[i][j - 1]);
                }
            }
        }
        return dp[k][n];
    }
};
