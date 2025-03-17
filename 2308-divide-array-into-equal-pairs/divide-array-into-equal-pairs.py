class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        ma = Counter(nums)
        a = [1 if ma[x] % 2 == 0 else 0 for x in ma.keys()]
        return sum(a) == len(a)