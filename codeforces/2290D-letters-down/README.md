# 2290D - Letters Down

https://codeforces.com/problemset/problem/2290/D

## Idea

An operation on x turns every x into x - 1, so letters only move down, one step at a time, and two letters never swap their order. The final value of a letter is a non-decreasing function of the letter.

For every mirrored pair s[i], s[n - 1 - i] with letters u < v, the two must end up equal. Since the mapping keeps the order, every letter from u to v must end up at the same value, so v has to walk down through v, v - 1, ..., u + 1. That needs one operation on each letter in (u, v].

So the answer is the number of letters c in b..z that lie in at least one range (u, v]. Doing the needed operations from z down to b uses each of them exactly once and makes every pair equal. A difference array over the 26 letters marks the covered ones.

## Complexity

O(n + 26) per test case, O(1) extra memory.
