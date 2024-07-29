class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        out = []

        for i in range(len(nums)):
            out.insert(index[i], nums[i])

        return out