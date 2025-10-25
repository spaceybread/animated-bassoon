class Solution:
    def ab(self, a, b): return (b * (b + 1) - a * (a + 1)) // 2

    def totalMoney(self, n: int) -> int:
        return sum([self.ab(i, i + 7) for i in range(n // 7)]) + self.ab((n // 7), (n // 7) + (n % 7))

         