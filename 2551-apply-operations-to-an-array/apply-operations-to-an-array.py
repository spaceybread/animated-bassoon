class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1): 
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        out = []
        for i in range(len(nums)):
            if nums[i] != 0: 
                out.append(nums[i])            
        out += [0] * (len(nums) - len(out))
        return out
