# 2243. Calculate Digit Sum of a String

https://leetcode.com/problems/calculate-digit-sum-of-a-string/

## Idea

Simulate the rounds. While the string is longer than k, cut it into groups of k characters (the last group may be shorter), replace each group by the sum of its digits written as a number, and join the results into the new string.

Each round makes the string shorter: a group of k ≥ 2 digits has a sum of at most 9k, which has fewer digits than k when k ≥ 2, so the loop always ends.

## Complexity

O(n) per round; the string shrinks quickly, so the total work is small for n ≤ 100. Memory O(n).
