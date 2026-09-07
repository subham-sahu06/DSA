class Solution:
    def distinctSubseqII(self, s):
        mod = 10**9 + 7
        end = [0] * 26
        for ch in s:
            idx = ord(ch) - 97
            end[idx] = (sum(end) + 1) % mod
        return sum(end) % mod