import random 

class Solution:

    def binary(self, num, length ): return format(num, '#0{}b'.format(length + 2))
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = set()

        for n in nums:
            s.add(int(n, 2))
        
        out = random.randint(0, 2**len(nums[0]) - 1)
        while out in s:
            out = random.randint(0, 2**len(nums[0]) - 1)

        print(out)
        sout = self.binary(out, len(nums[0]))[2:]

        return sout