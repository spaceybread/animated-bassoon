class Solution:
    def minLength(self, s: str) -> int:
        c = 0
        while "AB" in s or "CD" in s:
            s = s.replace("AB", "")
            s = s.replace("CD", "")
        return len(s)