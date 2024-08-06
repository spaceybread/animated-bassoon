class Solution:
    def minimumPushes(self, word: str) -> int:
        lc = [0] * 26
        for c in word:
            lc[ord(c) - ord('a')] += 1
        lc = sorted(lc)[::-1]

        c = 0
        for i, k in enumerate(lc):
            if k == 0:
                break
            c += (i // 8 + 1) * k
        
        return c