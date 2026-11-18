# 1524. Number of Sub-arrays With Odd Sum

https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

## Idea

The sum of a subarray is prefix[j] - prefix[i]. It is odd exactly when the two prefix sums have different parity.

Walk through the array and keep the running sum. Count how many prefix sums so far were odd and how many were even (the empty prefix 0 counts as one even). If the current prefix is odd, every earlier even prefix gives an odd subarray ending here, and the other way round.

Only the parity matters, so the running sum can never overflow in a way that changes the answer: with arr[i] <= 100 and length <= 10^5 the sum stays below 10^7.

## Complexity

O(n) time, O(1) memory.
