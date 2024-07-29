class Solution:
    def findLucky(self, arr: List[int]) -> int:
        li = sorted(arr)[::-1]
        p = -1
        c = 0

        for a in li:
            if a == p:
                c += 1
            else:
                if p != -1:
                    if p == c:
                        return c
                p = a
                c = 1
        
        if p == c:
            return c
        return -1            