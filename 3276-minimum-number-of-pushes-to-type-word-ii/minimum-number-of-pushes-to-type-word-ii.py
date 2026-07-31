from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq_map = Counter(word)
        sorted_counts = sorted(freq_map.values(), reverse=True)
        
        total_presses = 0
        idx = 0
        
        while idx < len(sorted_counts):
            presses_multiplier = (idx // 8) + 1
            total_presses += sorted_counts[idx] * presses_multiplier
            idx += 1
            
        return total_presses