class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        return [x for x in range(min(nums) + 1, max(nums)) if x not in nums]
        # return list(filter(lambda x : x > 0, [x if x not in nums else -1 for x in range(min(nums) + 1, max(nums))]))
        # return sorted(list(set(range(min(nums), max(nums))) - set(nums)))