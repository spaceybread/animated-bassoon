class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        li = [0] * len(nums)

        for n in nums:
            li[n - 1] += 1
        
        out = [0, 0]

        for i in range(len(li)):
            if li[i] == 0:
                out[1] = i + 1
            if li[i] == 2:
                out[0] = i + 1
        
        return out