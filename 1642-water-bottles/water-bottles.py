class Solution:
    def numWaterBottles(self, n: int, e: int) -> int:
        return n + (n - 1) // (e - 1)