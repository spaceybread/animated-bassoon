class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        bb, sb = -1, -2

        for x in nums:
            if x >= bb:
                sb = bb
                bb = x
            if bb > x >= sb:
                sb = x
            
        
        return (bb - 1) * (sb - 1)