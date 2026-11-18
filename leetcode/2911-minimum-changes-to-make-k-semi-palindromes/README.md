# 2911. Minimum Changes to Make K Semi-palindromes

https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/

## Idea

Two steps.

**1. Cost of one substring.** For every substring s[i..j] find the fewest changes that make it a semi-palindrome. Try every divisor d of its length with 1 ≤ d < length. For each remainder r, the characters at i + r, i + r + d, ... form one group; walk two pointers from both ends of the group and count the pairs that differ. Each differing pair needs one change. The cost of the substring is the smallest total over all d. A substring of length 1 has no valid d, so it can never be a part.

**2. Split into k parts.** dp[p][j] is the fewest changes for the first j characters split into p parts:

dp[p][j] = min over i < j of dp[p - 1][i] + cost[i][j - 1]

The answer is dp[k][n].

## Complexity

The costs take about O(n^3 log n) in the worst case (the number of divisors is small), and the DP takes O(k · n^2). With n ≤ 200 this is fast. Memory O(n^2).
