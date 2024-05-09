class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        l = sorted(happiness)

        h = 0
        for i in range(k):
            nex = l.pop(-1) - i
            if nex < 0:
                nex = 0
            h += nex
        return h