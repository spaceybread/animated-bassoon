class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a, b, r = 0, 0, 0
        l = min(x, y)
        
        for c in s:
            if c > 'b':
                r += min(a, b) * l
                a, b = 0, 0
            elif c == 'a':
                if x < y and b > 0:
                    b -= 1
                    r += y
                else:
                    a += 1
            elif c == 'b':
                if x > y and a > 0:
                    a -= 1
                    r += x
                else:
                    b += 1

        r += min(a, b) * l
        return r
