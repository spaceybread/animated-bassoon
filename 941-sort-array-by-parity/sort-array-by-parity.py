class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        eve = []
        odd = []

        for a in nums:
            if a % 2 == 0:
                eve.append(a)
            else:
                odd.append(a)
        
        return eve + odd