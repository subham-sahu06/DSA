# 2914. Minimum Number of Changes to Make Binary String Beautiful

https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

## Idea

Any even-length block of equal characters can be cut into blocks of length 2. So the string is beautiful exactly when every pair s[0..1], s[2..3], s[4..5], ... has two equal characters.

The pairs are independent: a pair with equal characters needs nothing, and a pair like "01" or "10" needs exactly one change. The answer is the number of pairs whose two characters differ.

## Complexity

O(n) time, O(1) extra memory.
