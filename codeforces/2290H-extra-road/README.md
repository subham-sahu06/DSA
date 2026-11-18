# 2290H - Extra Road

https://codeforces.com/problemset/problem/2290/H

## Idea

Root the tree at city 1. If a tree edge to child c is closed, the cities in the subtree of c are lost, unless the new road goes from inside that subtree to outside it. That happens exactly for the edges on the tree path between the two ends of the new road. Closing the new road itself loses nothing.

So we choose a path. The answer is n minus the largest subtree size of an edge that is not on the path.

The best path always goes through the root: it is either one chain down from the root, or two chains down into two different children of the root. Moving the path up toward the root never makes it worse.

Binary search on X, the largest subtree we allow to be lost. All edges with subtree size greater than X must be on the path. These edges form a connected part that hangs from the root. It fits on the path if the root has at most 2 such children and every other vertex has at most 1.

The answer is n minus the smallest X that works.

## Complexity

O(n log n) time, O(n) memory.
