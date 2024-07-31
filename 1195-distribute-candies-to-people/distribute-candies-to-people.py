class Solution:
    def distributeCandies(self, c: int, n: int) -> List[int]:
        l, i = [0] * n, 0
        while c >= 0:
            l[i % n] += min(i + 1, c)
            i += 1
            c -= i
        
        return l