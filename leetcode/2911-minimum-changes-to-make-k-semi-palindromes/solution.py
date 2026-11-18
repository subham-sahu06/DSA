class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = 10 ** 6
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                length = j - i + 1
                for d in range(1, length):
                    if length % d:
                        continue
                    changes = 0
                    for r in range(d):
                        lo, hi = i + r, i + length - d + r
                        while lo < hi:
                            if s[lo] != s[hi]:
                                changes += 1
                            lo += d
                            hi -= d
                    if changes < cost[i][j]:
                        cost[i][j] = changes
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for j in range(1, n + 1):
                best = INF
                for i in range(j):
                    if dp[p - 1][i] < INF and cost[i][j - 1] < INF:
                        best = min(best, dp[p - 1][i] + cost[i][j - 1])
                dp[p][j] = best
        return dp[k][n]
