class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        from collections import Counter
        st = Counter([x % 3 for x in stones])
        # print(st[0], st[1], st[2])

        if st[0] % 2 == 1: return abs(st[1] - st[2]) >= 3
        return min(st[1], st[2]) >= 1

        