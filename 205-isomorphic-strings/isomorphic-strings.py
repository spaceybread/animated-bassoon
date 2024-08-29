class Solution:
    def h(self, m):
        r = []
        for k, v in m.items(): r.append(v)
        return sorted(r)


    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sa, ta = {}, {}

        for i in range(len(s)):
            if s[i] not in sa: sa[s[i]] = [i]
            else: sa[s[i]] += [i]
            if t[i] not in ta: ta[t[i]] = [i]
            else: ta[t[i]] += [i]
        
        return self.h(sa) == self.h(ta)


