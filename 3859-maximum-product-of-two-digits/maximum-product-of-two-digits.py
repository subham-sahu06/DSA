class Solution:
    def maxProduct(self, n: int) -> int:
        digits = sorted([int(ch) for ch in str(n)], reverse=True)
        return digits[0] * digits[1]