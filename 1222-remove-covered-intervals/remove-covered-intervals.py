class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        sp = sorted(intervals, key = lambda x: (x[0], -x[1]))
        a, b = 0, 0

        for l, r in sp:
            a += 1 if r > b else 0
            b = max(b, r)
        
        return a