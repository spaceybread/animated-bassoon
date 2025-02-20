class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        n, d = len(s), [0] * (len(s) + 1)
        d[0], d[1] = 1, 1
        for i in range(2, n + 1):
            od, td = int(s[i - 1]), int(s[i - 2 : i])

            if od != 0: d[i] += d[i - 1]
            if 10 <= td <= 26: d[i] += d[i - 2]
        
        return d[n]
