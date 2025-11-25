class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        c = 0
        out = []
        for x in nums: 
            c += x
            out.append(c % 5 == 0)
            c = 2 * c
        return out