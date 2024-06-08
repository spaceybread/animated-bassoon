class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mep = {}
        mep[0] = -1
        rsum = 0

        for i in range(len(nums)):
            rsum += nums[i]
            m = rsum % k

            if mep.get(m) == None:
                mep[m] = i
            else:
                if i - mep[m] > 1:
                    return True
        return False
