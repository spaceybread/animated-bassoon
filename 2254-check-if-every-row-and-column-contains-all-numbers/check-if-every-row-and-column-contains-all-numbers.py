class Solution:
    def checkValid(self, m: List[List[int]]) -> bool:
        for r, c in zip(m, zip(*m)):
            if len(set(r)) != len(m) or len(set(c)) != len(m): return False
        return True
        