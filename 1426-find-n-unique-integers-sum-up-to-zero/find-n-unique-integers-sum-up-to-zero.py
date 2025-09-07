class Solution:
    def sumZero(self, n: int) -> List[int]:
        k = n // 2
        out = []
        for i in range(1, k + 1): out += [-i, i]

        if n % 2 == 1: out.append(0)

        return out