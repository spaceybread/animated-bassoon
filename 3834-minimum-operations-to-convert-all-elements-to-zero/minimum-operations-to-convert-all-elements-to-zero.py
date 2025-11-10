class Solution:
    def minOperations(self, nums: List[int]) -> int:
        st = [0] * (len(nums) + 1)
        t, a = 0, 0
        

        for n in nums:
            while st[t] > n:
                t -= 1
                a += 1
            if st[t] != n:
                t += 1
                st[t] = n

        return a + t