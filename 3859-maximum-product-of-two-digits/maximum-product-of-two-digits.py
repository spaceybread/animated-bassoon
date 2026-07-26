class Solution:
    def maxProduct(self, n: int) -> int:
        return int(sorted(list(str(n)))[-1]) * int(sorted(list(str(n)))[-2])