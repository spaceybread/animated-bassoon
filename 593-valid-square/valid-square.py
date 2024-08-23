class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        slopes = set()
        p = [p1, p2, p3, p4]

        for i in range(4):
            for j in range(i + 1, 4):
                slopes.add(dist(tuple(p[i]), tuple(p[j])))
        
        return len(slopes) == 2 and 0 not in slopes
        
        