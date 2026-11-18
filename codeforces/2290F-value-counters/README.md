# 2290F - Value Counters

https://codeforces.com/problemset/problem/2290/F

## Idea

Let value v stand at position i (0-indexed). Then b_v goes up once for every smaller value to its left, and down once for every larger value to its right.

Say a values smaller than v are to its left. The i values to the left of v are then a smaller ones and i - a larger ones. There are n - v larger values in total, so n - v - (i - a) of them are to the right. So

b_v = a - (n - v - i + a) = v + i - n

The unknown a cancels, so the position of every value is fixed:

i = b_v + n - v

Put each value v at that position. If a position is outside 0..n-1 or is used twice, there is no answer. Otherwise the positions form a permutation, and by the formula above it gives exactly the array b, so this answer is the only one.

## Complexity

O(n) time and memory.
