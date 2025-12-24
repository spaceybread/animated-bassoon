class Solution:
    def countOdds(self, low: int, high: int) -> int:
        x = (high - low) // 2
        if low % 2 == 1 or high % 2 == 1: x += 1

        return x

