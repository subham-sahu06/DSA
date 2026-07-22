import math
import bisect

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')
        
        ones_blocks = []
        i = 0
        while i < n:
            if s[i] == '1':
                j = i
                while j < n and s[j] == '1':
                    j += 1
                ones_blocks.append((i, j - 1))
                i = j
            else:
                i += 1
                
        num_blocks = len(ones_blocks)
        if num_blocks == 0:
            return [0] * len(queries)
            
        a_vals = [b[0] for b in ones_blocks]
        b_vals = [b[1] for b in ones_blocks]
        
        middle_gains = [0] * num_blocks
        for k in range(num_blocks):
            p = ones_blocks[k - 1][1] if k > 0 else -10**9
            q = ones_blocks[k + 1][0] if k < num_blocks - 1 else 10**9
            
            a_k, b_k = ones_blocks[k]
            len_k = b_k - a_k + 1
            middle_gains[k] = q - p - 1 - len_k
            
        log_n = int(math.log2(num_blocks)) + 1 if num_blocks > 0 else 1
        st = [[0] * num_blocks for _ in range(log_n)]
        
        for i in range(num_blocks):
            st[0][i] = middle_gains[i]
            
        for j in range(1, log_n):
            length = 1 << (j - 1)
            for i in range(num_blocks - (1 << j) + 1):
                st[j][i] = max(st[j - 1][i], st[j - 1][i + length])
                
        def get_rmq(L, R):
            if L > R:
                return -10**9
            length = R - L + 1
            k = int(math.log2(length))
            return max(st[k][L], st[k][R - (1 << k) + 1])
            
        ans = []
        for l, r in queries:
            k_start = bisect.bisect_right(a_vals, l)
            k_end = bisect.bisect_left(b_vals, r) - 1
            
            if k_start > k_end:
                ans.append(total_ones)
                continue
                
            best_gain = 0
            
            def compute_gain(k):
                a_k, b_k = ones_blocks[k]
                len_k = b_k - a_k + 1
                
                prev_1 = ones_blocks[k - 1][1] if k > 0 else -10**9
                next_1 = ones_blocks[k + 1][0] if k < num_blocks - 1 else 10**9
                
                left_bound = max(prev_1, l - 1)
                right_bound = min(next_1, r + 1)
                
                interval_len = right_bound - left_bound - 1
                return interval_len - len_k

            gain_start = compute_gain(k_start)
            if gain_start > best_gain:
                best_gain = gain_start
                
            gain_end = compute_gain(k_end)
            if gain_end > best_gain:
                best_gain = gain_end
                
            if k_start + 1 <= k_end - 1:
                mid_max = get_rmq(k_start + 1, k_end - 1)
                if mid_max > best_gain:
                    best_gain = mid_max
                    
            ans.append(total_ones + best_gain)
            
        return ans