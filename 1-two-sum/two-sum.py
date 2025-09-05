class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dm = {}
        for a in range(len(nums)): dm[nums[a]] = a
        subs = [(target - n) for n in nums]

        for i in range(len(subs)):
            if subs[i] in dm.keys():
                j = dm.get(subs[i])
                if i != j: return [i, j]
