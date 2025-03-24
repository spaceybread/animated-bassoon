class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        mtg = sorted(meetings)
        f, l = 0, 0

        for s, e in mtg:
            if s > l + 1: f += s - l - 1
            l = max(l, e)
        
        return f + days - l

        
