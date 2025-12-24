from bisect import bisect_left, bisect_right

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        ma = defaultdict(list)

        for i in range(len(nums)): ma[nums[i]] += [i]

        x = 0
        print(ma)
        for i in range(1, len(nums) - 1):
            l = nums[i] * 2 
            if l not in ma.keys(): continue

            pos = ma[l]
            l, r = bisect_left(pos, i), len(pos) - bisect_right(pos, i)
            x += l * r

        return x % (10**9 + 7)