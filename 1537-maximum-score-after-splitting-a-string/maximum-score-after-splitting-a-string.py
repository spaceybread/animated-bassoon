class Solution:
    def maxScore(self, s: str) -> int:
        z = [0, ]
        o = [0, ]

        for i in range(len(s)):
            if s[i] == '0':
                z.append(z[-1] + 1)
            else:
                z.append(z[-1])
        s = s[::-1]
        
        for i in range(len(s)):
            if s[i] == '1':
                o.append(o[-1] + 1)
            else:
                o.append(o[-1])
        
        z.pop(-1)
        z.pop(0)
        o.pop(-1)
        o.pop(0)
        o = o[::-1]
        
        out = -1

        for i in range(len(z)):
            t = o[i] + z[i]
            if t > out:
                out = t
        return out