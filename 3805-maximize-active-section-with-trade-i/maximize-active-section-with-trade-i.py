class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"
        
        runs = []
        curr = 1
        for i in range(1, len(t)):
            if t[i] == t[i - 1]:
                curr += 1
            else:
                runs.append(curr)
                curr = 1
        runs.append(curr)
        
        base_ones = 0
        for idx in range(0, len(runs), 2):
            base_ones += runs[idx]
        base_ones -= 2
        
        best = base_ones
        
        for i in range(2, len(runs) - 2, 2):
            candidate = base_ones + runs[i - 1] + runs[i + 1]
            if candidate > best:
                best = candidate
                
        return best