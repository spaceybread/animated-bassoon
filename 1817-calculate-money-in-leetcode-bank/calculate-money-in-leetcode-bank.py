class Solution:
    def ab(self, a, b):
        return (b * (b + 1) - a * (a + 1)) // 2

    def totalMoney(self, n: int) -> int:
        k = n // 7
        r = n % 7

        s = 0
        for i in range(k): s += self.ab(i, i + 7)
        
        s += self.ab(k, k + r)

        return s