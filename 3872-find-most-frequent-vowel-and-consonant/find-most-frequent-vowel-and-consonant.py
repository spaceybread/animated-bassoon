from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        ma = Counter(s)

        v_m = 0
        for a in 'aeiou':
            if ma.get(a) != None:
                v_m = max(v_m, ma.get(a))
        c_m = 0
        for a in ma.keys():
            if a not in 'aeiou' and ma.get(a) != None:
                c_m = max(c_m, ma.get(a))
        
        return v_m + c_m
