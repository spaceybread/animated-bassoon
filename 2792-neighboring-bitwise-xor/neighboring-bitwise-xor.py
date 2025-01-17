class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return (reduce(lambda r, x: r ^ x, derived , 0) == 0) or (reduce(lambda r, x: r ^ x, derived , 1) == 1)