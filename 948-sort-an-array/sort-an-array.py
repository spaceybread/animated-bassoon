class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        space = [0] * (10**5 + 2)

        for a in nums:
            space[a + 5 * 10**4] += 1
        
        out = []

        for i in range(len(space)):
            if space[i] > 0:
                for j in range(space[i]):
                    out.append(i - 5 * 10**4)

        return out

            
        