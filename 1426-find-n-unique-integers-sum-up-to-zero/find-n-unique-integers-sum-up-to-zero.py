class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        return [i for i in range(1, (n // 2) + 1)] + [-i for i in range(1, (n // 2) + 1)] + ([0] if n % 2 == 1 else [])

        # k = n // 2
        # out = []
        # for i in range(1, k + 1): out += [-i, i]

        # if n % 2 == 1: out.append(0)

        # return out