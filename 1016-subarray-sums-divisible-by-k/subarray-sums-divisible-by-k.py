class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        s, c, rsum = [0] * k, 0, 0
        s[0] = 1

        for i in range(len(nums)):
            rsum = (rsum + nums[i] % k + k) % k
            c += s[rsum]
            s[rsum] += 1

        return c
        


