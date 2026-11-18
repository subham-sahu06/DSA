# 2290E - Avalanche

https://codeforces.com/problemset/problem/2290/E

## Idea

Every stone is its own small game: taking a stone from pile i removes it and puts one new stone on each of the piles max(1, i - k) .. i - 1. So the whole game is a sum of independent stone games, and Sprague-Grundy applies.

Let g(i) be the Grundy value of one stone on pile i. A stone has exactly one possible move, and after it the position is the XOR of g(j) over j in [max(1, i - k), i - 1]. With a single option of value x, the mex is 1 if x = 0 and 0 otherwise:

g(i) = 1 if XOR of g over [max(1, i - k), i - 1] is 0, else 0

For pile 1 the range is empty, so g(1) = 1. A prefix XOR gives each range in O(1).

Two equal stones cancel in XOR, so pile i adds g(i) only when a_i is odd. Alice wins exactly when the XOR of g(i) over piles with odd a_i is not 0.

## Complexity

O(n) time and memory.
