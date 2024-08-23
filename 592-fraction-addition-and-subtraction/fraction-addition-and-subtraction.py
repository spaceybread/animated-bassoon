class Solution:
    def fractionAddition(self, expression: str) -> str:
        import re
        from fractions import Fraction
        f, val = [(int(n), int(d)) for n, d in re.findall("([+-]?\d+)/(\d+)", expression)], 0
        
        num, den = 0, 1

        for n, d in f:
            num = num * d + n * den
            den *= d
        
        g = gcd(abs(num), den)

        num, den = num // g, den // g

        return str(num) + "/" + str(den)
            