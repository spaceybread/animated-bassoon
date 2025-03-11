class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        out, lp = 0, {"a": -1, "b": -1, "c": -1}
        for i in range(len(s)):
            lp[s[i]] = i
            out += 1 + min(lp.values())
        return out