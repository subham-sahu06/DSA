class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        # Compress values so a Fenwick tree can store them by rank.
        values = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(values)}
        m = len(values)
        count = [0] * (m + 1)
        total = [0] * (m + 1)

        def update(i, c, s):
            while i <= m:
                count[i] += c
                total[i] += s
                i += i & -i

        def prefix(i):
            c = s = 0
            while i > 0:
                c += count[i]
                s += total[i]
                i -= i & -i
            return c, s

        def kth_smallest(target):
            pos = 0
            step = 1 << m.bit_length()
            while step:
                nxt = pos + step
                if nxt <= m and count[nxt] < target:
                    pos = nxt
                    target -= count[nxt]
                step >>= 1
            return pos + 1

        # cost[i] = moves to make nums[i : i + x] all equal (move everything to the median).
        cost = [0] * (n - x + 1)
        window_sum = 0
        for i, v in enumerate(nums):
            update(rank[v], 1, v)
            window_sum += v
            if i >= x:
                old = nums[i - x]
                update(rank[old], -1, -old)
                window_sum -= old
            if i >= x - 1:
                r = kth_smallest((x + 1) // 2)
                median = values[r - 1]
                below_count, below_sum = prefix(r)
                above_count = x - below_count
                above_sum = window_sum - below_sum
                cost[i - x + 1] = (median * below_count - below_sum) + (above_sum - median * above_count)

        # dp[i] = best cost using the first i elements with j windows chosen so far.
        INF = float("inf")
        prev = [0] * (n + 1)
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(j * x, n + 1):
                cur[i] = min(cur[i - 1], prev[i - x] + cost[i - x])
            prev = cur
        return prev[n]