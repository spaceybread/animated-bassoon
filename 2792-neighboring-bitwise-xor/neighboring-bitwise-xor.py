class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        s = 0
        for a in derived: s ^= a
        if s == 0: return True

        s = 1
        for a in derived: s ^= a
        if s == 1: return True

        return False