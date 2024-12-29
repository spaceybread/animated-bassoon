from functools import cache

class Solution:
    @cache
    def f(self, a, b, c):
        if a < 0 or b < 0: return 0
        if self.s[a] == self.t[b]: return self.f(a - 1, b - 1, c) + (c == 0)
        return 0 if c == 0 else 1 + self.f(a - 1, b - 1, 0)
    
    def countSubstrings(self, s: str, t: str) -> int:
        self.s, self.t = s, t
        return sum(self.f(a, b, 1) for a in range(len(s)) for b in range(len(t)))