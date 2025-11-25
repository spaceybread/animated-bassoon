class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        c = 0
        out = []
        for x in nums: 
            c += x
            if c % 5 == 0: out.append(True)
            else: out.append(False)
            c = 2 * c
        return out