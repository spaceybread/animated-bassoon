class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        e = sorted(heights)
        c = 0
        for i in range(len(heights)):
            if e[i] != heights[i]:
                c += 1
        return c