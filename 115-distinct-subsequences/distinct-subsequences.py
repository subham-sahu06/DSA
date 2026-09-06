class Solution:
    def numDistinct(self, s, t):
        n, m = len(s), len(t)
        f = [1] + [0] * m
        for ch in s:
            for j in range(m, 0, -1):
                if ch == t[j - 1]:
                    f[j] += f[j - 1]
        return f[m]