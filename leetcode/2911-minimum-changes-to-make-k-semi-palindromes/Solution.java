class Solution {
    public int minimumChanges(String s, int k) {
        int n = s.length();
        final int INF = 1_000_000;
        int[][] cost = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int len = j - i + 1;
                int best = INF;
                for (int d = 1; d < len; d++) {
                    if (len % d != 0) continue;
                    int changes = 0;
                    for (int r = 0; r < d; r++) {
                        int lo = i + r, hi = i + len - d + r;
                        while (lo < hi) {
                            if (s.charAt(lo) != s.charAt(hi)) changes++;
                            lo += d;
                            hi -= d;
                        }
                    }
                    best = Math.min(best, changes);
                }
                cost[i][j] = best;
            }
        }
        int[][] dp = new int[k + 1][n + 1];
        for (int[] row : dp) java.util.Arrays.fill(row, INF);
        dp[0][0] = 0;
        for (int p = 1; p <= k; p++) {
            for (int j = 1; j <= n; j++) {
                for (int i = 0; i < j; i++) {
                    if (dp[p - 1][i] >= INF || cost[i][j - 1] >= INF) continue;
                    dp[p][j] = Math.min(dp[p][j], dp[p - 1][i] + cost[i][j - 1]);
                }
            }
        }
        return dp[k][n];
    }
}
