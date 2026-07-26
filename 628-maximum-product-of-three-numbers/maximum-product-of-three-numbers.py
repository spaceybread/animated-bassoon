class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a, b, c = -100000, -1100000, -1100000
        x, y = 1000000, 1000000

        for n in nums:
            aa, bb, xx = a, b, x
            a, b, c = max(a, n), max(b, min(aa, n)), max(c, min(bb, n))
            x, y = min(x, n), min(y, max(xx, n))
        
        return max(a * b * c, a * x * y)
    