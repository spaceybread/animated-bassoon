import math

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ns, n = sorted(arr), len(arr)
        m, l = math.inf, []

        for i in range(n - 1): 
            diff = ns[i + 1] - ns[i]

            if diff < m:
                m = diff 
                l = []

            if diff == m: l += [[ns[i], ns[i + 1]]]

        
        return l