from functools import cache

class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        suf = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1] + piles[i]

        @cache
        def solve(i, m):
            if i + 2 * m >= n:
                return suf[i]
            return suf[i] - min(solve(i + x, max(m, x)) for x in range(1, 2 * m + 1))

        return solve(0, 1)