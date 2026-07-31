class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter as ct
        p1, p2, p3, p4 = 8, 8, 8, 2
        w = list(word)
        cw = ct(w)
        ls = sorted(list(set(w)), key = lambda x : cw[x])[::-1]

        c = 0
        for i in range(len(ls)):
            x = ls[i]
            if i < 8: c += cw[x]
            elif 8 <= i < 16: c += 2 * cw[x]
            elif 16 <= i < 24: c += 3 * cw[x]
            else: c += 4 * cw[x]
        return c