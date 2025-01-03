class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        rev = nums[::-1]
        up, down = [], []

        for i in range(len(nums)): 
            up.append(nums[i] + up[-1]) if len(up) > 0 else up.append(nums[i])
            down.append(rev[i] + down[-1]) if len(down) > 0 else down.append(rev[i])
        
        up, down = up[:-1], down[:-1][::-1]
        c = 0
        for i in range(len(up)):
            if up[i] >= down[i]: c += 1
        
        return c