from bisect import bisect_right 

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        evs = sorted(events)
        n, suf = len(evs), [evs[-1][2]] * len(evs)
        sol = 0

        for i in range(n - 2, -1, -1): suf[i] = max(suf[i + 1], evs[i][2])

        for k in evs:
            et, va = k[1], k[2]
            idx = bisect_right(evs, et, key = lambda x : x[0])
            if idx < n: va += suf[idx]
            sol = max(sol, va)

        return sol
            