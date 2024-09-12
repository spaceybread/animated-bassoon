class Solution:
    def countConsistentStrings(self, a: str, w: List[str]) -> int:
        s, c = set(a), 0

        for wi in w:
            if all(ch in s for ch in wi): c+= 1
        
        return c
